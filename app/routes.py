from app import app


@app.route('/')
@app. route('/index')
def index():
    return "Hello World!"

@app. route('/french')
def french():
    return "bonjour tout le monde!"
