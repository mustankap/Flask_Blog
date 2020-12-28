from flask import Flask,render_template,url_for,flash,redirect
from forms import RegistrationForm,LoginForm
app = Flask(__name__)

app.config['SECRET_KEY']='sdfghjkjhgfxcvbn345678765432'

postlists = [
    {
        'author':'Mustansir',
        'title':'First Blog',
        'content':'Demagogues',
        'date_posted':' 6th April 2020'
    },
    {
        'author':'Mustansir',
        'title':'First Blog',
        'content':'Demagogues',
        'date_posted':'23rd April 2020'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=postlists)

@app.route('/about')
def about():
    return render_template('about.html',title = 'about')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Account created for {}!'.format({form.username.data}),'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'register', form = form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'mustankap@gmail.com' and form.password.data == 'fire':
            flash('you have been logged in','success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccesfull.Please check username and password again.','danger')


    return render_template('login.html', title = 'register', form = form)

if __name__=='__main__':
    app.run(debug=True)
