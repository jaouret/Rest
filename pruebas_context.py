#>>> from hello import app
#>>> from flask import current_app
#>>> current_app.name
#Traceback (most recent call last):
#...

#RuntimeError: working outside of application context
#push is mandatory to make contexts available to the thread

#>>> app_ctx = app.app_context()
#>>> app_ctx.push()
#>>> current_app.name
#'hello'
#>>> app_ctx.pop()

from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent