from flask import Flask, render_template, request

Menu = Flask(__name__)
@Menu.route('/')
def login():
    return render_template("login.html")

@Menu.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        get_Name = request.form["nme"]
        get_Branch = request.form["brn"]
        get_AdmnNum = request.form["admnnum"]
        get_RollNum = request.form["rollnum"]
        get_DOB = request.form["dob"]
        get_Sem = request.form["sem"]
        get_Pass = request.form["pass"]
        get_ConfPass = request.form["confpass"]
        print(get_Name)
        print(get_Branch)
        print(get_AdmnNum)
        print(get_RollNum)
        print(get_DOB)
        print(get_Sem)
        print(get_Pass)
        print(get_ConfPass)
    return render_template("register.html")

@Menu.route('/search')
def search():
    return render_template("search.html")

@Menu.route('/delete')
def delete():
    return render_template("delete.html")

if __name__ == "__main__":
    Menu.run()