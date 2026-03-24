"""
NGO Content Management System - Main Application Entry Point
"""

import os
from flask import Flask, render_template

# Import extensions from extensions module
from extensions import db, login_manager, bcrypt, csrf, mail


def create_app(config_name='default'):
    """Application factory pattern for creating Flask app"""
    
    # Create Flask application
    app = Flask(__name__)
    
    # Load configuration
    from config import get_config
    app.config.from_object(get_config())
    
    # Initialize extensions with app
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    csrf.init_app(app)
    mail.init_app(app)
    
    # Configure login manager
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'
    login_manager.session_protection = 'strong'
    
    @login_manager.user_loader
    def load_user(user_id):
        """Load user by ID for Flask-Login"""
        from models import User
        return User.query.get(int(user_id))
    
    # Create upload folder if not exists
    upload_folder = app.config.get('UPLOAD_FOLDER', 'static/uploads')
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    
    # Register blueprints (routes)
    from routes.main import main_bp
    from routes.auth import auth_bp
    from routes.admin import admin_bp
    from routes.user import user_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(user_bp, url_prefix='/user')
    
    # Context processor to provide contact info to all templates
    @app.context_processor
    def inject_contact():
        """Make contact info available to all templates"""
        return {
            'contact': type('obj', (object,), {
                'phone': '+1 234 567 8900',
                'email': 'info@hopefoundation.org',
                'address': '123 Hope Street, City, Country'
            })()
        }
    
    # Create database tables and default admin
    with app.app_context():
        from models import User, Donation, Content, Volunteer, Event, Report
        db.create_all()
        
        # Create default admin if not exists
        create_default_admin()
    
    # Error handlers
    @app.errorhandler(404)
    def error_404(error):
        return render_template('errors/404.html'), 404
    
    @app.errorhandler(500)
    def error_500(error):
        db.session.rollback()
        return render_template('errors/500.html'), 500
    
    return app


def create_default_admin():
    """Create default admin user if not exists"""
    from models import User
    
    admin = User.query.filter_by(email='admin@ngo.org').first()
    if not admin:
        admin = User(
            full_name='System Administrator',
            email='admin@ngo.org',
            role='admin',
            status='active'
        )
        admin.set_password('admin123')
        db.session.add(admin)
        db.session.commit()
        print("Default admin created: admin@ngo.org / admin123")
    return admin


# Run the application
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)