#register new user gui
from tkinter import *
import mysql.connector
from tkinter import messagebox as mb


register = Tk()
register.title("Register new user")
register.resizable(False, False)

db = mysql.connector.connect(
    user="lifechoices",
    password="@Lifechoices1234",
    host="localhost",
    database="lifechoicesonline",
    auth_plugin="mysql_native_password"
)

cursor = db.cursor()

db.commit()


def show():
    psswrd.config(show="")



nameregisterLb = Label(register, text="Full Name:", fg="white", bg="black")
nameregister = Entry(register)
usrNamelb = Label(register, text="Username:", fg="white", bg="black")
psswrdlb = Label(register, text="Password:", fg="white", bg="black")

usrName = Entry(register)
psswrd = Entry(register, show='*')


def addUser():
    try:
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS users(id int(11) Not null primary key AUTO_INCREMENT, full_name varchar(60) Default null, "
            "username varchar(50) Default null ,password varchar(20) Default null)")
        user_info = (nameregister.get(), str(usrName.get()), str(psswrd.get()))
        comm = "INSERT INTO users (full_name, username, password) VALUES (%s, %s, %s)"

        cursor.execute(comm, user_info)

        db.commit()
        mb.showinfo("Confirmation", "User Created Successfully")
        register.destroy()
        import main

    except:
        mb.showerror("error", "Username already exist")
        register.destroy()
        import main


def back():
    register.destroy()
    import main


cBtn = Button(register, text="Create student", command=addUser)
bBtn = Button(register, text="Back", command=back)

nameregisterLb.place(x=10, y=100)
nameregister.place(x=90, y=100)
usrNamelb.place(x=10, y=140)
usrName.place(x=90, y=140)
psswrdlb.place(x=10, y=180)
psswrd.place(x=90, y=180)
cBtn.place(x=10, y=220)
bBtn.place(x=350, y=220)


register.config(bg="black")
register.geometry("400x270")
register.mainloop()
