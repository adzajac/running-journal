from app import create_app, db
from app.models import User, Run
from config import Config
import unittest


class configForTests(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite://"


class UserModelCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        self.app = create_app(configForTests)
        
        
    def test_password(self):
        u = User()
        correct_pass = 'abcdefgh123asdfS'
        wrong_pass = 'xbcdefgh123asdfS'
        u.set_password(correct_pass)
        self.assertTrue(u.check_password(correct_pass))
        self.assertFalse(u.check_password(wrong_pass))
     
    
    def test_new_user(self):
        with self.app.app_context():
            u = User(username="mark", email="mark@example.com")
            db.session.add(u)
            db.session.commit()
            get_user = User.query.filter_by(username="mark").first()
            self.assertEqual(get_user.username, u.username)
            self.assertEqual(get_user.email, u.email)
            
            
           
    @classmethod
    def tearDownClass(self):
        with self.app.app_context():
            db.drop_all()
     
    
    
if __name__ == '__main__':
    unittest.main()
