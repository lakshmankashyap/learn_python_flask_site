from flask import  Flask

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

if __name__ == '__main__':
    app.run()