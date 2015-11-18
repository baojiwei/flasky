from flask import Flask, render_template
#from flask.ext.script import Manager
from flask import make_response
from flask import redirect
from flask import abort
from flask import request
from flask.ext.bootstrap import Bootstrap


app = Flask(__name__)
#manager = Manager(app)

@app.route('/')
def index_test():
    # to void too many arguments in view , we can use request
    #user_agent = request.headers.get('User_Agent')
    #return '<h1> Hello World! Your browser is %s</h1>' % user_agent
    return render_template('index.html')

@app.route('/user/<name>')
def user_test(name):
    # get string from URI
    return render_template('user.html',name=name)

@app.route('/null')
def null_test():
    return '<h1>Bad Request</h1>', 400

@app.route('/response')
def response_test():
    #response = make_response('<h1>This document carries a cookie!</h1>')
    #response.set_cookie('answer','42')
    #return response


@app.route('/redirect')
def redirect_test():
    return redirect('http://baidu.com')

@app.route('/usererror/<id>')
def abort_test(id):
    if(id!='1'):
        abort(404)
    return '<h1>Hello,%s</h1>'%id

if __name__=='__main__':
    #manager.run()
    app.run()
