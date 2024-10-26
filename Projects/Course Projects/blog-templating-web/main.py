from flask import Flask, render_template
import requests

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=posts)

@app.route("/post/<post_no>")
def get_post(post_no):
    requested_post = None
    for post in posts:
        if post["id"] == int(post_no):
            requested_post = post
    
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
