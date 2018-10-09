
## A very simple Flask Hello World app for you to get started with...
## --- below is the default generated app from pythonanywhere's Flask install

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello from Flask!</h1><a href="./hello">Say hello again</a>'

@app.route('/hello')
def hello():
    return '''
        <p>say hello again</p>
        <p><a href="/">go home</a></p>
        '''
if __name__ == '__main__':
    app.run(debug=True)

##import os
##
##from flask import Flask
##
##@app.route('/')
##def hello_world():
##    return 'Hello from Flask! <a href="./hello">Say hello again</a>'
##
##
##def create_app(test_config=None):
##    # create and configure the app
##    app = Flask(__name__, instance_relative_config=True)
##    app.config.from_mapping(
##        SECRET_KEY='dev',
##        DATABASE=os.path.join(app.instance_path, 'flaskrsqlite'),
##        )
##    if test_config is None:
##        # load the instance config, if it exists, when NOT testing
##        app.config.from_pyfile('config.py', silent=True)
##    else:
##        # load the test config if passed in
##        app.config.from_mapping(test_config)
##
##    # ensure the instance folder exists
##    try:
##        os.makedirs(app.instance_path)
##        except OSERROR:
##            pass
##    # a simple page that says hello
##    @app.route('/hello')
##    def hello():
##        return 'Hello, World!'
##
##    return app