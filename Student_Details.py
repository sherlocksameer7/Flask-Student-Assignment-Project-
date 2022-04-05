from flask import Flask, render_template, request
import sqlite3

connection = sqlite3.connect("student_data.db", check_same_thread=False)
table = connection.execute("Select name from sqlite_master where type='table' and name='student'").fetchall()
if table != []:
    print("Table Already Exists")

else:
    connection.execute('''Create Table student(
                          ID Integer Primary Key Autoincrement,
                          Name text,
                          Branch text,
                          Roll_Num integer,
                          Admn_Num integer,
                          DOB text,
                          Semester text,
                          Password text
    );''')

    print("Table Created")

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

        try:
            query = "Insert into student(Name, Branch, Roll_Num, Admn_Num, DOB, Semester, Password) \
                    Values('"+get_Name+"', '"+get_Branch+"', "+get_RollNum+", "+get_AdmnNum+", '"+get_DOB+"', '"+get_Sem+"', '"+get_Pass+"')"
            print(query)
            connection.execute(query)
            connection.commit()
            connection.close()
            print("Data Added Successfully")
        except Exception as err:
            print("Error Occured", err)

    return render_template("register.html")

@Menu.route('/search')
def search():
    return render_template("search.html")

@Menu.route('/delete')
def delete():
    return render_template("delete.html")

if __name__ == "__main__":
    Menu.run()