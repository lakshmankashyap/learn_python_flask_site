from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

'''
@app.route('/')
def hello():
    return 'hello world'
'''
@app.route('/')
def index():
    return render_template('hello.html')

# @app.route('/welcome/<username>')
# def index(username):
#     return render_template('hello.html',name=username)

@app.route('/new')
def new():
    return 'new page'


@app.route('/demo')
def demo():
    return 'this is demo page'


# @app.route('/profile/<name>')
@app.route('/profile/<int:id>')
# def profile(name):
def profile(id):
    # return 'This profile belongs to %s' %name
    return 'This profile belongs to %d' % id


def demo():
    return 'this is demo page'


@app.route('/admin')
def hello_admin():
    return 'Hello admin'


@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello guest %s' % guest


@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hell0_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))
    return 'Hello guest %s' % guest

@app.route('/success/<name>')
def success(name):
    return "welcome %s" %name

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method =='POST':
        username = request.form['nm']
        return redirect(url_for('success',name=username))
    else:
        username = request.args.get('nm')
        return redirect(url_for('success'), name = username)
@app.route('/student')
def student():
    return render_template('student.html')

@app.route('/result', methods=['POST','GET'])
def result():
    if request.method =='POST':
        result = request.form
        return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run()
