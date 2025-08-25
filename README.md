What we’re building (quick map)
Frontend (React + Bootstrap/Tailwind + Leaflet + Recharts)
Public Landing Page (hero, value props, how it works, CTA).
Auth: Login/Register (Resident, Company, Admin).
Dashboards:
Resident: request pickup, track status, view history, report dumping.
Company: assigned pickups, live route map, update statuses.
Admin: real-time queue, KPIs, map of incidents/trucks, users, zones, reports.
Real-time UI: toast alerts + live tiles (WebSockets/polling).
Map: Live truck markers + incidents (Leaflet + OSM).
Backend (Django + DRF + Channels + CORS)
APIs: auth (JWT), pickups, schedules, trucks (GPS), dumping reports, notifications.
WebSockets: admin alerts, live truck positions, status updates.
SMS (provider placeholder): schedule reminders, “truck approaching”, incident acks.
DB: SQLite3 (dev) → PostgreSQL (prod).

FEATURES
User registration/login (citizens, companies, admins)
Waste pickup request form
Interactive city map with collection zones (optional GIS)
Real-time dashboard for admin (pending requests, collection status)
Email notifications
Complaint and feedback system
Waste pickup history
Payment tracking (optional)
Admin panel for assigning routes and managing users

SYSTEM SETUP GUIDE
🐍 BACKEND – DJANGO + SQLITE3
Install Python & Virtual Environment

Install Django and Required Packages
sudo apt install python3 python3-pip python3-venv  # For Linux
python3 -m venv my_venv
source my_venv/bin/activate  # On Windows: cleanug_env\Scripts\activate
django-admin startproject core .
pip install requirements.txt

1) Project structure Backend
WASTE_MANAGEMENT_CLEANUG/
└── backend/
    ├── manage.py
    ├── requirements.txt
    ├── core/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── accounts/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── serializers.py
    │   ├── urls.py
    │   └── views.py
    ├── waste/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── serializers.py
    │   ├── urls.py
    │   └── views.py
    ├── operations/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── serializers.py
    │   ├── urls.py
    │   └── views.py
    └── notifications/
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── consumers.py
        ├── routing.py
        ├── urls.py
        ├── views.py
        └── sms.py
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

Smoke test (APIs):
Register: POST /api/accounts/register/
Token: POST /api/accounts/token/ → get access
Auth header: Authorization: Bearer <access>
Create pickup: POST /api/waste/pickups/
KPIs: GET /api/ops/kpis/

WebSockets (in browser devtools to test):

// Admin alerts
let ws1 = new WebSocket("ws://127.0.0.1:8000/ws/admin/alerts/");
ws1.onmessage = e => console.log("ALERT:", e.data);

// Truck positions
let ws2 = new WebSocket("ws://127.0.0.1:8000/ws/trucks/positions/");
ws2.onmessage = e => console.log("TRUCK:", e.data);


Send an alert as admin:

curl -X POST -H "Authorization: Bearer <ADMIN_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"title":"System Ready","message":"Clean UG backend up"}' \
  http://127.0.0.1:8000/api/notify/alert/


Ingest a truck position:

curl -X POST -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"truck":1,"lat":0.3476,"lng":32.5825}' \
  http://127.0.0.1:8000/api/ops/telemetry/
      END OF BACKEND AND API
      
