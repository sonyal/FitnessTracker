from app import db, app
from models import User, Plan
import unittest
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import create_engine

class TestDatabase(unittest.TestCase):

    def test_add_user(self):
        db.init_app(app)

        with app.app_context():
            new_user = User(username="bob", password=generate_password_hash("testpassword123456", method='sha256'),
                                weight="70", height="180")
            db.session.add(new_user)
            db.session.commit()

            comfirm_user = User.query.filter_by(username="bob").first()
        self.assertEqual(new_user, comfirm_user)
    
    def test_delete_user(self):
        db.init_app(app)

        with app.app_context():
            user = User.query.filter_by(username="bob").first()

            db.session.delete(user)
            db.session.commit()

            comfirm_user = User.query.filter_by(username="bob").first()
        self.assertEqual(comfirm_user, None)