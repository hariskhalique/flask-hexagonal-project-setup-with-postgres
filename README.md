# Flask Application with SQLAlchemy and Migrations

This is a Flask application with a modular architecture, utilizing SQLAlchemy for ORM and Flask-Migrate for database migrations. The application is designed to be easily extensible and maintainable.

---

## **Features**

- Modular structure for controllers, services, and repositories.
- SQLAlchemy for ORM (Object-Relational Mapping).
- Flask-Migrate for database schema migrations.
- UUID-based primary keys for `Order` and `Product` entities.
- Thread-safe database connection using Singleton design pattern.
- Relationships between `User`, `Order`, and `Product`.

---

## **Prerequisites**

Ensure you have the following installed:

- Python 3.8+
- PostgreSQL
- pip (Python package manager)

---

## **Setup**

### **1. Clone the Repository**

```bash
git clone <repository-url>
cd <repository-name>
```

### **2 Create a Virtual Environment**

```bash
python -m venv venv
```

Activate the virtual environment:
- On Windows:
```base
venv\Scripts\activate
```
- On macOS/Linux:
```base
source venv/bin/activate
```

### **3 Install Dependencies**
```base
pip install -r requirements.txt
```

### **4 Configure Environment Variables**
Create a .env file in the project root and add the following:
```
FLASK_ENV=development 
FLASK_DEBUG=1 
DATABASE_URL=postgresql://<username>:<password>@localhost/<database_name>
```

### **5 Set FLASK_APP Environment Variable**
Set the FLASK_APP variable to specify the application entry point:
- On Windows:
```
set FLASK_APP=app.main:create_app
```
- On macOS/Linux:
```
export FLASK_APP=app.main:create_app
```

### **6 Initialize the Database**
Run the following commands to set up the database:
1. Initialize Migrations:
```
flask db init
```
2. Update code in .env file in migration folder
```
def get_metadata():
    return database.Base.metadata
```
3. Generate Migration Scripts:
```
flask db migrate -m "Initial migration"
```
4. Apply Migrations:
```
flask db upgrade
```

### **6 Run the Application**
```
flask run
```

### **7 Verify the Application**
```
http://127.0.0.1:5000/
```

```
project/
│
├── app/
│   ├── adapters/
│   │   ├── in/
│   │   │   ├── http/
│   │   │   │   ├── controllers.py
│   │   ├── out/
│   │   │   ├── database/
│   │   │   │   ├── entities/
│   │   │   │   ├── model.py
│   │   │   │   ├── db.py
│   │   │   ├── repositories.py
│   ├── application/
│   │   ├── application_module.py
│   ├── config/
│   │   ├── config.py
│   │   ├── exception/
│   │   ├── logging/
│   ├── domain/
│   │   ├── services/
│   │   │   ├── service.py
│   ├── app_module.py
│   ├── main.py
├── migrations/
├── requirements.txt
├── .env
├── README.md
```