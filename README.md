# Remind-me-later 🕒💬

A simple Django-based backend API for scheduling reminders. Users can create reminders by providing a message, date, time, and method of delivery (SMS or Email). This project focuses only on accepting and storing reminders via an API — actual delivery (SMS/email sending) is not included.

---

## 📌 Features

- Accept reminders through a clean API endpoint.
- Store date, time, message, and delivery method (SMS or Email).
- Easily extendable for future delivery methods.
- Clean and modular Django structure.
- Ready for front-end integration.

---

## 🔧 Tech Stack

- Python 3.x
- Django 4.x
- Django REST Framework

---

remind-me-later/
├── manage.py
├── remind_me_later/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── reminders/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ ├── urls.py
│ └── migrations/
├── requirements.txt
└── README.md








