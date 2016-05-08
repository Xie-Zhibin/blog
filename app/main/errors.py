from . import main

@main.app_errorhandler(404)
def notFound(e):
    return "404", 404

@main.app_errorhandler(500)
def internalError(e):
    return "500", 500