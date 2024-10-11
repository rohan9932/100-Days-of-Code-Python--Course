from flask import Flask, render_template, request
from smtplib import SMTP
import requests

MY_EMAIL = "test.rohan932@gmail.com"
PASSWORD = "sutaqythfkmgsaku"

posts = requests.get("https://api.npoint.io/bc986ba19f658a338890").json()

def send_message(mail, message):
    my_email = MY_EMAIL
    my_pass = PASSWORD
    
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_pass)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=mail,
            msg=f"Subject:Message\n{message}"
        )

app = Flask(__name__)

@app.route("/")
def get_all_posts():
    return render_template("index.html", all_posts= posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        mail_address = data["email"]
        message = data["message"]
        send_message(mail_address, message)

        return render_template("contact.html", received=True)
    
    elif request.method == "GET":
        return render_template("contact.html", received=False)


@app.route("/posts/<int:post_id>")
def see_post(post_id):
    requested_post = None
    for post in posts:
        if post["id"] == post_id:
            requested_post = post
    
    return render_template("post.html", post=requested_post)
    

if __name__ == "__main__":
    app.run(debug=True)
