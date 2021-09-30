from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Welcome page')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/post')
def post():
    return render_template('post.html', title='Post')

if __name__ == '__main__':
    app.debug = True
    app.run()