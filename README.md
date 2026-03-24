# NGO Content Management System

This is a Flask-based web application for NGO content management, donation handling, and volunteer coordination.

## Setup Instructions

### 1. Install Required Dependencies

```bash
pip install flask flask-login flask-sqlalchemy flask-bcrypt flask-wtf email-validator flask-mail chart.js
```

Or use the requirements file:
```bash
pip install -r requirements.txt
```

### 2. Configure MySQL Database

Create a MySQL database named `ngo_cms`:

```sql
CREATE DATABASE ngo_cms;
```

Update the database configuration in `config.py` if needed:
- Default: `mysql://root:password@localhost/ngo_cms`
- Update with your MySQL credentials

### 3. Initialize the Database

Run the application once to create all tables:
```bash
python app.py
```

### 4. Access the Application

- **Admin Login**: `http://localhost:5000/admin/login`
- **Default Admin Credentials**: `admin@ngo.org` / `admin123`
- **User Portal**: `http://localhost:5000/`

### 5. Features

- User authentication (register, login, password reset)
- Role-based access control (Admin/User)
- Content Management System (blogs, news, reports)
- Donation handling with Razorpay integration
- Volunteer and event management
- Dashboard analytics with Chart.js
- Responsive Bootstrap-based UI

## Project Structure

```
/project
 ├── app.py                 # Main application entry point
 ├── config.py              # Configuration settings
 ├── models/                # Database models
 │   ├── __init__.py
 │   ├── user.py
 │   ├── donation.py
 │   ├── content.py
 │   ├── volunteer.py
 │   └── event.py
 ├── routes/                # Flask blueprints/routes
 │   ├── __init__.py
 │   ├── auth.py
 │   ├── admin.py
 │   ├── user.py
 │   └── main.py
 ├── templates/             # HTML templates
 ├── static/                # CSS, JS, images
 │   ├── css/
 │   ├── js/
 │   └── images/
 └── database/              # SQL scripts
     └── schema.sql
```

## Technologies Used

- **Backend**: Flask (Python)
- **Database**: MySQL with SQLAlchemy ORM
- **Frontend**: Bootstrap 5, Custom CSS
- **Charts**: Chart.js
- **Authentication**: Flask-Login
- **Security**: Bcrypt password hashing, CSRF protection

## License

MIT License