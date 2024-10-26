from flask import Flask, render_template
import random
from datetime import datetime
import requests

# Running the website
app = Flask(__name__)

@app.route("/")
def home():
    random_num = random.randint(1,50)
    current_year = datetime.now().year
    return render_template("index.html", num=random_num, year=current_year)


@app.route("/<username>")
def guess(username):
    parameters = {
        "name": username.title(),
    }

    # Extracting gender and age
    agify_response = requests.get("https://api.agify.io", params=parameters)
    age = agify_response.json()["age"]
    genderize_response = requests.get("https://api.genderize.io", params=parameters)
    gender = genderize_response.json()["gender"]

    return render_template("guess.html", name=username, age=age, gender=gender)


@app.route("/blog/<blog_num>")
def get_blog(blog_num):
    print(blog_num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    
    return render_template("blog.html", posts=all_posts)


# Run the website
if __name__ == "__main__":
    app.run(debug=True)

