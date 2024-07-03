from flask import Flask, render_template, url_for
from forms import SignUpForm
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = '244352'
db = SQLAlchemy(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(80), nullable=False)

websites = {
    'about_us': 'about_us.html',
    'contact_us': 'contact_us.html',
    'app': 'index.html',
    'login': 'login.html',
    'register': 'register.html',
}

@app.route('/')
def load_main_website():
    return render_template(websites['app'])

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/<website_name>')
def load_website(website_name):
    if website_name in websites:
        return render_template(websites[website_name])
    else:
        return "Website not found"

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        return 'Thank you for signing up!'
    return render_template('signup.html', form=form)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)