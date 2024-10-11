# For detailed info head over to the official documentation: "https://flask.palletsprojects.com/en/3.0.x/"

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return ("<h1 style='text-align: center'>Hello, World!</h1>"
            "<p style='text-align: center'>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the "
            "industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and"
            " scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap "
            "into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the"
            " release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing "
            "software like Aldus PageMaker including versions of Lorem Ipsum.</p>"
            "<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMHRodmR4d3lkMmZlNDB1c2djOXAxNmNmZThxMXNnbWt5MnFtaj"
            "VzZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/dRvEZLV0ORAmHT1L5u/giphy.gif'>")

# task
def make_bold(func):
    def wrapper_func():
        return "<b>"+ func() + "</b>"
    return wrapper_func

def make_emphasis(func):
    def wrapper_func():
        return "<em>" + func() + "</em>"
    return wrapper_func

def make_underline(func):
    def wrapper_func():
        return "<u>" + func() + "</u>"
    return wrapper_func

@app.route("/bye")
@make_bold
@make_underline
@make_emphasis
def say_bye():
    return "<p>Bye</p>"

@app.route("/<name>/<int:number>")
def greet(name, number):
    return f"<h1>Hello {name}. You are {number} years old.</h1>"

if __name__ == "__main__":
    # Run the app in debug mode to auto reload
    app.run(debug=True)

# @app.route('/')
# def index():
#     return 'Index Page'
#
# @app.route('/hello')
# def hello():
#     return '<p>Hello, World</p>'
