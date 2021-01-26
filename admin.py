#admin login gui
import mysql.connector
from tkinter import messagebox as mb
from tkinter import *
from datetime import *
import os


admin_login = Tk()
admin_login.resizable(False, False)
admin_login.title("Admin login")



db = mysql.connector.connect(
    user="lifechoices",
    password="@Lifechoices1234",
    host="localhost",
    database="lifechoicesonline",
    auth_plugin="mysql_native_password"
)
cursor=db.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS admin(id int(11) Not null primary key AUTO_INCREMENT, full_name varchar(60) Default null, "
    "username varchar(50) Default null ,password varchar(20) Default null)")
db.commit()

cursor.execute("INSERT INTO admin(full_name, username, password) \
   SELECT * FROM (SELECT 'lifechoices', 'user', '@Lifechoices1234') as temp \
   WHERE NOT EXISTS \
   (SELECT 'lifechoices' FROM admin WHERE username = 'lifechoices') LIMIT 1")

db.commit()


def login():
    usr = usrEnt.get()
    p = adUps.get()
    sql = "select * from admin where username=%s and password=%s"
    cursor.execute(sql, [(usr), (p)])
    datab = cursor.fetchall()

    if datab:
        mb.showinfo("Login", "login successful")
        admin_login.destroy()
        import admingui
    else:
        mb.showerror("Unsuccessful", "Login failed")

def back():
    admin_login.destroy()
    import main

bckbtn = Button(admin_login, text="Back", command=back)
enterbtn = Button(admin_login, text="Login", command=login)

admnlbl = Label(admin_login, text="Username:", fg="green", bg="black")
usrEnt = Entry(admin_login)
admpassw = Label(admin_login, text="Password:", fg="green", bg="black")
adUps = Entry(admin_login)
admnlbl.place(x=20, y=100)
usrEnt.place(x=150, y=100)
admpassw.place(x=20, y=140)
adUps.place(x=150, y=140)
enterbtn.place(x=20, y=180)
bckbtn.place(x=320, y=180)

lf = LabelFrame(admin_login, bg="black")
lf.pack(fill="both")

lbl = Label(lf, text="ADMIN ONLY", height=2, fg="green", bg="white")
lbl.pack()

admin_login.geometry("400x240")
admin_login.configure(bg="black")
admin_login.mainloop()
