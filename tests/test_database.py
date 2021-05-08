from app import db
from models import User, Plan
import unittestc

class TestDatabase(unittest.TestCase):
    def test_add_user():
        new_user = User(username="bob", password=generate_password_hash("testpassword123456", method='sha256'),
                                weight="70", height"180")
        db.session.add(new_user)
        db.session.commit()

        comfirm_user = db.query.filter_by(username="bob").first()
        self.assertEqual(new_user, comfirm_user)
    
    def test_delete_user():
        user = db.query.filter_by(username="bob").first()

        db.session.delete(user)
        db.session.commit()

        comfirm_user = db.query.filter_by(username="bob").first()
        self.assertEqual(comfirm_user, None)