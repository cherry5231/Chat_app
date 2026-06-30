from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    login_required,
    logout_user,
    current_user,
)
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)

app.config["SECRET_KEY"] = "change_this_to_a_random_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


# -----------------------------
# Database Models
# -----------------------------

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(50), unique=True, nullable=False)

    email = db.Column(db.String(100), unique=True, nullable=False)

    password = db.Column(db.String(200), nullable=False)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(50), nullable=False)

    text = db.Column(db.Text, nullable=False)

    time = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# -----------------------------
# Home
# -----------------------------

@app.route("/")
def home():
    if current_user.is_authenticated:
        return redirect("/chat")
    return redirect("/login")


# -----------------------------
# Login
# -----------------------------

@app.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:
        return redirect(url_for("chat"))

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):

            login_user(user)

            return redirect(url_for("chat"))

        return "Invalid email or password!"

    return render_template("login.html")


# -----------------------------
# Signup
# -----------------------------

@app.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        # Check if username already exists
        if User.query.filter_by(username=username).first():
            return "Username already exists!"

        # Check if email already exists
        if User.query.filter_by(email=email).first():
            return "Email already registered!"

        hashed_password = generate_password_hash(password)

        new_user = User(
            username=username,
            email=email,
            password=hashed_password
        )

        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)

        return redirect(url_for("chat"))

    return render_template("signup.html")
# -----------------------------
# Chat
# -----------------------------

@app.route("/chat")
@login_required
def chat():
    return render_template(
        "chat.html",
        username=current_user.username
    )
@app.route("/send", methods=["POST"])
@login_required
def send():

    text = request.form["message"].strip()

    if text == "":
        return "Empty message", 400

    msg = Message(
        username=current_user.username,
        text=text
    )

    db.session.add(msg)
    db.session.commit()

    return "OK"
@app.route("/messages")
@login_required
def messages():

    msgs = Message.query.order_by(Message.time).all()

    data = []

    for msg in msgs:

       
            data.append({
        "id": msg.id,
        "username": msg.username,
        "text": msg.text,
        "time": msg.time.strftime("%H:%M"),
        "mine": msg.username == current_user.username
    })

    return jsonify(data)

# -----------------------------
# Logout
# -----------------------------

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/login")
@app.route("/delete/<int:message_id>", methods=["POST"])
@login_required
def delete_message(message_id):

    message = Message.query.get_or_404(message_id)

    if message.username != current_user.username:
        return "Unauthorized", 403

    db.session.delete(message)
    db.session.commit()

    return "Deleted"

import os

if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )
