from tkinter import *
#login gui
import mysql.connector
from tkinter import messagebox as mb
from datetime import *
import os
import sys


db = mysql.connector.connect(
    user="lifechoices",
    password="@Lifechoices1234",
    host="localhost",
    database="",
    auth_plugin="mysql_native_password"
)

cursor = db.cursor()
cursor.execute("create database if not exists lifechoicesonline")
cursor.execute("use lifechoicesonline")
cursor.execute("CREATE TABLE IF NOT EXISTS time_in(full_name varchar(60) Default null, date date, logged_in time)")
db.commit()
cursor.execute("CREATE TABLE IF NOT EXISTS time_out(full_name varchar(60) Default null, date date, logged_out time)")
db.commit()

def restart():
    py = sys.executable
    os.execl(py, py, * sys.argv)
def showAdmin():
    root.destroy()
    import admin


def login():
    usrr = usernm.get()
    s = psw.get()
    sql = "select * from users where username=%s and password=%s"
    try:
        cursor.execute(sql, [(usrr), (s)])
        db.commit()
    except:
        mb.showerror("Error","Error in SQL")
        root.destroy()
        restart()
    datab = cursor.fetchall()
    if datab:
        mb.showinfo("Message", "Login successfully")
        root.destroy()
        login1 = datetime.now()
        z = login1.strftime("%H:%M:%S")
        dt = login1.strftime("%d/%m/%y")
        time1 = usrr, str(dt),  str(z)
        comm_time1 = "INSERT INTO time_in(full_name, date, logged_in)VALUES (%s, %s, %s)"
        cursor.execute(comm_time1, time1)
        db.commit()

        window = Tk()
        window.title("Logout")
        window.geometry("400x200")


        windowlbl = Label(window, text="mobile Number", bg="black", fg="white")
        windowlbl.place(x=10, y=100)

        window_ent = Entry(window)
        window_ent.place(x=130, y=100)

        def logg_out():

            logout = datetime.now()
            z= logout.strftime("%H:%M:%S")
            time1 = usrr, str(dt), str(z)
            comm_time1 = "INSERT INTO time_out(full_name, date, logged_out)VALUES (%s, %s, %s)"
            cursor.execute(comm_time1, time1)
            db.commit()
            mb.showinfo("Login", "logout successful")
            window.destroy()

        log_out = Button(window, text="sign out", command=logg_out)
        log_out.place(x=180, y=160)

    else:
        mb.showerror("Unsuccessful", "Login failed")


def newuser():
    root.destroy()
    import register


root = Tk()
root.resizable(False, False)
root.title("Login")


userlbl = Label(root, text="Username:",fg="white", bg="black")
pswlbl = Label(root, text="Password:",fg="white", bg="black")
usernm = Entry(root)
psw = Entry(root, show='*')




btn = Button(root, text="register", width=10, command=newuser)

btnLogin = Button(root, text="login", width=10, command=login)


userlbl.place(x=10, y=40)
usernm.place(x=85, y=40)
pswlbl.place(x=10, y=80)
psw.place(x=85, y=80)
btn.place(x=180, y=150)
btnLogin.place(x=60, y=150)


root.bind("<Control-a>", lambda i: showAdmin())
root.configure(bg="grey")
root.geometry("400x270")
root.mainloop()

