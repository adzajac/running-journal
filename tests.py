from app import create_app, db
from app.models import User
from config import Config
import unittest


class configForTests(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite://"


class UserModelCase(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app(configForTests)
        
    def test_password(self):
        u = User()
        correct_pass = 'abcdefgh123asdfS'
        wrong_pass = 'xbcdefgh123asdfS'
        u.set_password(correct_pass)
        self.assertTrue(u.check_password(correct_pass))
        self.assertFalse(u.check_password(wrong_pass))
        
        
        
if __name__ == '__main__':
    unittest.main()
