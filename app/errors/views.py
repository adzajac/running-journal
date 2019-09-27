from app.errors import blueprint
from flask import render_template

@blueprint.app_errorhandler(404)
def error_404(error):
    return render_template("errors/404.html")


@blueprint.app_errorhandler(500)
def error_500(error):
    return render_template("errors/500.html")