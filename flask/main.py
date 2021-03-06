from flask import Flask,render_template
from werkzeug.contrib.fixers import ProxyFix
app = Flask(__name__,static_url_path='/static',template_folder='templates')

@app.route('/')
def root():
    return render_template('init/index.html') 


app.wsgi_app = ProxyFix(app.wsgi_app)
if __name__ == '__main__':
    app.run(debug=True)
