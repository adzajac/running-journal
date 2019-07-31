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
            
    def test_add_run(self):
        with self.app.app_context():
            u = User(username="john", email="john@examaple.com")
            db.session.add(u)
            db.session.commit()
            run_1 = Run(user_id=u.id, distances="1000", times="600")
            run_2 = Run(user_id=u.id, distances="2000", times="1200")
            run_3 = Run(user_id=u.id, distances="3000", times="1800")
            db.session.add(run_1)
            db.session.add(run_2)
            db.session.add(run_3)
            db.session.commit()
            self.assertEqual(len(u.runs.all()),3)
            self.assertEqual(u.runs.first().distances,"1000")
            self.assertEqual(u.runs.first().times,"600")
            
           
    @classmethod
    def tearDownClass(self):
        with self.app.app_context():
            db.drop_all()
     
    
    
if __name__ == '__main__':
    unittest.main()
