from flask import  Flask, redirect, url_for

app =  Flask(__name__)

@app.route('/')
def hello():
    return  'hello world'

@app.route('/new')
def new():
    return 'new page'

@app.route('/demo')
def demo():
    return 'this is demo page'

#@app.route('/profile/<name>')
@app.route('/profile/<int:id>')
#def profile(name):
def profile(id):
    #return 'This profile belongs to %s' %name
    return 'This profile belongs to %d' %id

def demo():
    return 'this is demo page'

@app.route('/admin')
def hello_admin():
    return 'Hello admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello guest %s' %guest

@app.route('/user/<name>')
def hello_user(name):
    if name =='admin':
        return redirect(url_for('hell0_admin'))
    else:
        return redirect(url_for('hello_guest',guest=name))
    return 'Hello guest %s' %guest



if __name__ == '__main__':
    app.run()