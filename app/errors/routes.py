from app.errors import blueprint


@blueprint.app_errorhandler(404)
def error_404(error):
    return "Page not found"


@blueprint.app_errorhandler(500)
def error_500(error):
    return "Unexpected error"