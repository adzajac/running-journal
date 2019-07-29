from app.extensions import db
from app.models import User,Run,Injury

from datetime import datetime

def init_database(app):
    with app.app_context():
        db.create_all()
        
def sample_data(app):
    with app.app_context():
        u1 = User(username="John", email="abcdef@example.com")
        u1.set_password('12345')
        u2 = User(username="Sarah", email="abcdef2@example.com")
        u2.set_password('12345')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        distances = [8000, 11400, 5000, 15100, 4200, 10000, 12000, 14000, 11000, 15600, 12200, 13300, 14000, 12000, 10000, 15600, 12200, 13300, 14000, 12000, 10000, 15600, 12200, 13300]
        times = [1400, 1800, 2100, 2000, 2250, 3300, 1300, 1000, 4300, 2900, 2100, 2300, 2300, 2000, 1800, 2900, 2100, 2300, 2300, 2000, 1800, 2900, 2100, 2300]
        timestamp = [datetime(2019, 5, 6), datetime(2019, 5, 10), datetime(2019, 5, 12), datetime(2019, 5, 16), datetime(2019, 5, 19), datetime(2019, 5, 21), datetime(2019, 5, 25), datetime(2019, 5, 27), datetime(2019, 6, 1), datetime(2019, 6, 4), datetime(2019, 6, 8), datetime(2019, 6, 10),datetime(2019, 6, 16), datetime(2019, 6, 20), datetime(2019, 6, 23), datetime(2019, 6, 28), datetime(2019, 7, 2), datetime(2019, 7, 6),datetime(2019, 7, 13), datetime(2019, 7, 16), datetime(2019, 7, 19), datetime(2019, 7, 21), datetime(2019, 7, 24), datetime(2019, 7, 26)]
        for i in range(len(distances)):
            run = Run(user_id=u1.id, distances=str(distances[i]), times=str(times[i]), timestamp=timestamp[i])
            db.session.add(run)
            db.session.commit()