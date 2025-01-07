from app import app

from flask import render_template, request, redirect, jsonify, make_response

from datetime import datetime

@app.template_filter("clean_date")
def clean_date(dt):
    return dt.strftime("%d %b %Y")

@app.route("/")
def index():
    return render_template("/public/index.html")

@app.route("/jinja")
def jinja():

    my_name = "Dylan"

    age = 17

    langs = ["Python", "JavaScript", "Bash", "C", "Ruby"]

    friends = {
        "Tom": 30,
        "Amy": 60,
        "Tony": 56,
        "Clarissa": 23
    }

    colors = ("Red", "Green")

    cool = False

    class GitRemote:
        def __init__(self, name, description, url):
            self.name = name
            self.description = description
            self.url = url

        def pull(self):
            return f"Pullin repo {self.name}"
        
        def clone(self):
            return f"Cloning into {self.url}"

    my_remote = GitRemote(
        name="Flask Jinja",
        description="Template design tutorial",
        url="https://github.com/dylink006/flask-tutorial.git"

    )

    def repeat(x, qty):
        return x * qty

    date = datetime.utcnow()

    my_html = "<h1>THIS IS SOME HTML</h1>"

    suspicious = "<script>alert('YOU GOT HACKED')</script>"

    return render_template("public/jinja.html", my_name=my_name, age=age,
    langs=langs, friends=friends, colors=colors, cool=cool, GitRemote=GitRemote,
    repeat=repeat, my_remote=my_remote, date=date, my_html=my_html, suspicious=suspicious
    )

@app.route("/about")
def about():
    return render_template("/public/about.html")

@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():

    if request.method == "POST":

        req = request.form

        username = req["username"]
        email = req.get("email")
        password = request.form["password"]

        print(username, email, password)

        return redirect(request.url)


    return render_template("public/sign-up.html")

users = {
    "dylan": {
        "name": "Dylan McGarry",
        "twitter_handle": "@dylink006"
    },
    "elonmusk": {
        "name": "Elon Musk",
        "twitter_handle": "@elonmusk"
    }
}

@app.route("/profile/<username>")
def profile(username):

    user = None

    if username in users:
        user = users[username]
    
    return render_template("public/profile.html", user=user, username=username)

@app.route("/multiple/<foo>/<bar>/<baz>")
def multi(foo, bar, baz):
    return f"foo is {foo}, bar is {bar}, baz is {baz}"

@app.route("/json", methods=["POST"])
def json():
    
    if request.is_json:
        req = request.get_json()

        response = {
            "message": "JSON received!",
            "name": req.get("name")
        }

        res = make_response(jsonify(response), 200)

        return res
    else:
        res = make_response(jsonify({"message": "No JSON received"}), 400)

        return res

@app.route("/guestbook")
def guestbook():
    return render_template("public/guestbook.html")

@app.route("/guestbook/create-entry", methods=["POST"])
def create_entry():
    req = request.get_json()

    print(req)

    res = make_response(jsonify(req), 200)


    return res