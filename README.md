# Chat Box Messenger
link - https://chatapp-production-a65a.up.railway.app/login?next=%2Fchat
A modern real-time-style web chat application built with **Flask**, **SQLite**, **Flask-Login**, and **JavaScript**. Users can create accounts, log in securely, send messages, and interact through a clean and responsive chat interface.

---

##  Features

*  Secure user authentication

  * User registration
  * Login & logout
  * Password hashing with Werkzeug

*  Global chat room

  * Send messages instantly
  * Automatic message refresh
  * View all chat history

*  Message management

  * Delete your own messages
  * Protected against deleting other users' messages

* Modern UI

  * Responsive design
  * Clean chat layout
  * Mobile-friendly interface

---

##  Tech Stack

* **Backend:** Flask
* **Database:** SQLite (Flask-SQLAlchemy)
* **Authentication:** Flask-Login
* **ORM:** SQLAlchemy
* **Frontend:** HTML5, CSS3, JavaScript
* **Password Security:** Werkzeug

---

##  Project Structure

```text
Chat-Box-Messenger/
│
├── app.py
├── Procfile
├── requirements.txt
├── .gitignore
│
├── instance/
│   └── database.db
│
├── templates/
│   ├── login.html
│   ├── signup.html
│   └── chat.html
│
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── chat.js
```

---


## Authentication

Passwords are never stored in plain text.

The application uses Werkzeug's secure password hashing to protect user credentials.

---

##  Future Improvements

* Multiple chat rooms
* Private messaging
* User profile pictures
* Emoji support
* File and image sharing
* Typing indicators
* Online/offline user status
* Message editing
* PostgreSQL support
* WebSocket-based real-time messaging

---

##  Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

##  License

This project is open source and available under the MIT License.

---

##  Author

**Charan**

If you found this project useful, consider giving it a ⭐ on GitHub!
