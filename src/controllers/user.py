from src import app

@app.route('/user/<username>', methods=['GET'])
def profile(username):
    app.logger.debug('Acess method profile by ' + username)
    return '{}\'s profile'.format(username)