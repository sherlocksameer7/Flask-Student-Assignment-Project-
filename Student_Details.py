from flask import Flask, render_template

Menu = Flask(__name__)
@Menu.route('/')
def login():
    return render_template("login.html")

@Menu.route('/register')
def register():
    return render_template("register.html")

@Menu.route('/search')
def search():
    return render_template("search.html")

@Menu.route('/delete')
def delete():
    return render_template("delete.html")

if __name__ == "__main__":
    Menu.run()