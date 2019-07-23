from app.errors import error_bp


@error_bp.app_errorhandler(404)
def error_404(error):
    return "Page not found"


@error_bp.app_errorhandler(500)
def error_500(error):
    return "Unexpected error"