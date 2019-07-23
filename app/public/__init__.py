from flask import Blueprint


blueprint = Blueprint('public', __name__, 
                      template_folder='templates', static_folder='static')


from app.public import views
