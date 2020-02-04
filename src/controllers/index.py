from src import app

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, World!'

@app.errorhandler(500)
def internal_error(error):
    return 'error 500'

@app.errorhandler(404)
def not_found_error(error):
    return 'error 404'