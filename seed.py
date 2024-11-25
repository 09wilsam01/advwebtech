from models import db, User
from flask_bcrypt import Bcrypt
from app import app

bcrypt = Bcrypt(app)

with app.app_context():
    db.create_all()  # Ensures the database and tables are created
    
    # Check if a user already exists to avoid duplicate entries
    if not User.query.filter_by(username='testuser').first():
        hashed_password = bcrypt.generate_password_hash('testpassword').decode('utf-8')
        new_user = User(username='testuser', password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        print("Test user added successfully!")
    else:
        print("Test user already exists.")