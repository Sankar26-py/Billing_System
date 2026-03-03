Django Billing System:

A simple Django-based Billing System application with asynchronous invoice email sending using Celery and Redis.

---

TECH STACK:

Python
Django
SQLite
Celery
Redis
HTML / CSS / JavaScript

---

SETUP INSTRUCTIONS:

1. Create Virtual Environment

  Run:
  python -m venv env
  
  Activate virtual environment:
  
  venv\Scripts\activate

---

2. Install Dependencies

Run:
pip install -r requirements.txt

---

3. Apply Migrations

  Run:
  python manage.py migrate

---

4. Create Superuser (For Admin Access)

  Run:
  python manage.py createsuperuser

  Admin URL:
  [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

5. Run Django Server

  Run:
  python manage.py runserver
  
  Application URL:
  [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

ASYNC EMAIL SETUP (CELERY + REDIS):

  Step 1: Start Redis Server
  
  Run:
  redis-server
  
  Keep this terminal open.

---

Step 2: Start Celery Worker (Windows)

  Run:
  celery -A billing_system_project worker --loglevel=info --pool=solo


---

WHY --pool=solo?

  Windows does not support Celery’s default prefork pool.
  --pool=solo runs Celery in single-thread mode.
  It is required for Windows compatibility.

---

RUNNING ORDER:

Open three terminals:

  Terminal 1:
  redis-server
  
  Terminal 2:
  celery -A billing_system worker --loglevel=info --pool=solo
  
  Terminal 3:
  python manage.py runserver

---

EMAIL TESTING:

  Console email backend is used for development.
  Emails will appear in the Django server terminal instead of being sent to a real inbox.

---

FEATURES:

  * Product management via Admin
  * Dynamic billing page
  * Tax calculation
  * Rounded net price calculation
  * Denomination-based balance calculation
  * Purchase history
  * Asynchronous invoice email sending
  * Database integrity using unique_together

---

Author
Sankar K
