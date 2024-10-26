from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

class MyForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), Email(message="Enter a valid email address")])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=8, message="Field must be atleast 8 characters long")])
    log_in = SubmitField(label="Log In")


app = Flask(__name__)
bootstrap = Bootstrap5(app)

app.secret_key = "adlfkajdoifhefjdknf"

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        user_email = "admin@email.com"
        user_pass = "12345678"
        if user_email == form.email.data and user_pass == form.password.data:
            return render_template("success.html")
        else:
            return render_template("denied.html")
        
    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
