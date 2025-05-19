# 🚀 Django REST API Project

This is a Django REST API project that includes models, views, and serializers to manage various resources like user authentication, application statuses, file uploads, and calendar events.

## ✨ Features
- 🔐 **User Authentication**: Login and Signup functionality using Django's authentication system.
- 📄 **Application Management**: CRUD operations on applications, with status options of ✅ "Accept" or ❌ "Reject".
- 🎵 **Audio Upload**: File upload functionality for audio files.
- 📅 **Calendar Events**: Manage calendar events with details like date, time, and event name.

## 🛠️ Technologies Used
- 🐍 Python 3.8+
- 🌐 **Django 5.2.1**
- 🔧 **Django REST Framework**
- 🐘 **PostgreSQL** (or SQLite for development)
- 🌍 **CORS Headers** for cross-origin requests

---

## ⚙️ Installation

### ✅ Prerequisites
- Python 3.8 or higher
- Django 5.2.1
- PostgreSQL (if using for production)

### 🧩 Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/your-repository-name.git
   cd your-repository-name
Create and activate a virtual environment:

On Windows:

bash
Copy code
python -m venv env
env\Scripts\activate
On macOS/Linux:

bash
Copy code
python3 -m venv env
source env/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Configure your database:

SQLite (Default): No configuration needed.

PostgreSQL: Update DATABASES in settings.py like:

python
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
Apply migrations:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Run the development server:

bash
Copy code
python manage.py runserver
🌐 API Endpoints
Endpoint	Description
/api/login/	🔑 Login view
/api/signup/	🆕 Signup view
/api/input/	📝 Input data
/api/input1/	📝 Additional input data
/api/upload/	🎵 Upload audio files
/api/applications/	📄 Manage applications (Accept/Reject)
/api/calendar/	📅 Calendar events CRUD

📦 Example Data
To create an application with status:

json
Copy code
{
  "applicant_name": "John Doe",
  "status": "Accept"
}
json
Copy code
{
  "applicant_name": "Jane Smith",
  "status": "Reject"
}
🧪 Testing
Use Django's test client or Postman to test all API endpoints.

Ensure CRUD operations work as expected for each model.

📁 File Uploads
Media files (like audio) are handled via the AudioUpload model.

Configure your MEDIA_URL and MEDIA_ROOT in settings.py accordingly:

python
Copy code
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
🔐 CORS Configuration
In settings.py, enable CORS:

python
Copy code
CORS_ALLOW_ALL_ORIGINS = True
For production:

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

🤝 Contributing
Contributions are welcome! Fork the repository, submit issues, or create pull requests.

🙏 Acknowledgments
💡 Django

🔌 Django REST Framework

🧪 Postman

Output images had been uploded







