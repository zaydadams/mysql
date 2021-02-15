#admin gui
import mysql.connector
from tkinter import messagebox as mb
from tkinter import *
import subprocess


admin = Tk()
admin.resizable(False, False)
admin.title("Adminastrator")
db = mysql.connector.connect(
    user="lifechoices",
    password="@Lifechoices1234",
    host="localhost",
    database="lifechoicesonline",
    auth_plugin="mysql_native_password"
)

cursor = db.cursor()


def show():
    selction = var.get()
    if selction == 1:
        cursor.execute("SELECT id FROM admin")

        idi = cursor.fetchall()

        for x in idi:
            lisname.insert(END, x)

        lisname.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT full_name FROM admin")

        name = cursor.fetchall()

        for x in name:
            liD.insert(END, x)

        liD.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT username FROM admin")

        uname = cursor.fetchall()
        for x in uname:
            liT.insert(END, x)
        liT.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT password FROM admin")

        pas = cursor.fetchall()
        for x in pas:
            liP.insert(END, x)
        liP.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT full_name FROM time_in")

        tun = cursor.fetchall()
        for x in tun:
            Liu.insert(END, x)
        Liu.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT date FROM time_in")

        d = cursor.fetchall()
        for x in d:
            Lid.insert(END, x)
        Lid.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT logged_in FROM time_in")

        time_used = cursor.fetchall()
        for x in time_used:
            LiTi.insert(END, x)
        LiTi.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT logged_out FROM time_out")

        timeout = cursor.fetchall()
        for x in timeout:
            LiT0.insert(END, x)
        LiT0.insert(END, str(cursor.rowcount) + " rows")

    elif selction == 2:
        cursor.execute("SELECT id FROM users")

        idi = cursor.fetchall()

        for x in idi:
            lisname.insert(END, x)

        lisname.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT full_name FROM users")

        name = cursor.fetchall()

        for x in name:
            liD.insert(END, x)

        liD.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT username FROM users")

        uname = cursor.fetchall()
        for x in uname:
            liT.insert(END, x)
        liT.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT password FROM users")

        pas = cursor.fetchall()
        for x in pas:
            liP.insert(END, x)
        liP.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT full_name FROM time_in")

        tun = cursor.fetchall()
        for x in tun:
            Liu.insert(END, x)
        Liu.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT date FROM time_in")

        d = cursor.fetchall()
        for x in d:
            Lid.insert(END, x)
        Lid.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT logged_in FROM time_in")

        time_used = cursor.fetchall()
        for x in time_used:
            LiTi.insert(END, x)
        LiTi.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT logged_out FROM time_out")

        time_used = cursor.fetchall()
        for x in time_used:
            LiT0.insert(END, x)
        LiT0.insert(END, str(cursor.rowcount) + " rows")

def add():
    selction = var.get()
    if selction == 1:
        comm3 = "INSERT INTO admin (full_name, username, password) VALUES (%s, %s, %s)"
        user_info1 = str(regname.get()), str(usrName.get()), psswrd.get()
        cursor.execute(comm3, user_info1)
        db.commit()
        mb.showinfo("Confirmation", "Admin created successfully")

    elif selction == 2:
        comm3 = "INSERT INTO users (full_name, username, password) VALUES (%s, %s, %s)"
        user_info1 = str(regname.get()), str(usrName.get()), psswrd.get()
        cursor.execute(comm3, user_info1)
        db.commit()
        mb.showinfo("Confirmation", "User created successfully")


def delete():
    selction = var.get()
    if selction == 1:
        fullname=usrName.get()
        Delete="delete from admin where full_name='%s'" %(fullname)
        cursor.execute(Delete)
        Delete="delete from time_in where full_name='%s'" %(fullname)
        cursor.execute(Delete)
        Delete="delete from time_out where full_name='%s'" %(fullname)
        cursor.execute(Delete)
        db.commit()
        mb.showinfo("Information","Record Deleted")


    elif selction == 2:
        fullname = usrName.get()
        Delete = "delete from users where full_name='%s'" % (fullname)
        cursor.execute(Delete)
        db.commit()
        mb.showinfo("Information", "Record Deleted")

def clear():
    lisname.delete(0,END)
    liD.delete(0,END)
    liT.delete(0,END)
    liP.delete(0,END)
    Liu.delete(0, END)
    Lid.delete(0,END)
    LiTi.delete(0, END)
    LiT0.delete(0,END)


def grant():
    selection = var.get()
    if selection == 1:
        priv_com = "GRANT ALL PRIVILEGES ON lifechoicesonline.* TO username = %s @'localhost"
        cursor.execute(priv_com)
        mb.showinfo("Message", "Privileges Granted")
    elif selection >=2:
        mb.showerror("Attention", "Admin users online")

def count():
    selection = var.get()
    if selection == 1:
        cursor = db.cursor()
        query = "SELECT count(*) FROM admin"
        cursor.execute(query)
        myresult = cursor.fetchall()
        total = ('Total number of admin users logged in\n',(myresult[-1][-1]))
        mb.showinfo("Attention", total)
    elif selection == 2:
        cursor = db.cursor()
        query = "SELECT count(*) FROM users"
        cursor.execute(query)
        myresult = cursor.fetchall()
        total = ('Total number of users logged in\n', (myresult[-1][-1]))
        mb.showinfo("Attention", total)



lblid = Label(admin, text="ID:", fg="white", bg="black")
lisname = Listbox(admin, width=15, height=6)
lblfn = Label(admin, text="Fullname:", fg="white", bg="black")
liD = Listbox(admin, width=15, height=6)
lbluser = Label(admin, text="Username", fg="white", bg="black")
liT = Listbox(admin, width=15, height=6)
lblpassw = Label(admin, text="Password:",fg="white", bg="black")
liP = Listbox(admin, width=15, height=6)


#######################################
labele = Label(admin, text="Username:",fg="white", bg="black")
Liu = Listbox(admin, width=15, height=6)
lbD = Label(admin, text="Date:", fg="white", bg="black")
Lid = Listbox(admin, width=15, height=6)
LiTiL = Label(admin, text="Login Time:", fg="white", bg="black")
LiTi = Listbox(admin, width=15, height=6)
LiOl = Label(admin, text="Logout Time:", fg="white", bg="black")
LiT0 = Listbox(admin, width=15, height=6)


regislbl = Label(admin, text="Full Name:",fg="white", bg="black")
regname = Entry(admin)
usrNamelb = Label(admin, text="Username:",fg="white", bg="black")
psswrdlb = Label(admin, text="Password:",fg="white", bg="black")

usrName = Entry(admin)
psswrd = Entry(admin, show='*')


lblid.place(x=260, y=270)
lisname.place(x=260, y=300)
lblfn.place(x=390, y=270)
liD.place(x=390, y=300)
lbluser.place(x=520, y=270)
liT.place(x=520, y=300)
lblpassw.place(x=650, y=270)
liP.place(x=650, y=300)
#
labele.place(x=260, y=420)
Liu.place(x=260, y=450)
lbD.place(x=390, y=420)
Lid.place(x=390, y=450)
LiTiL.place(x=520, y=420)
LiTi.place(x=520, y=450)
LiOl.place(x=650, y=420)
LiT0.place(x=650, y=450)

regislbl.place(x=10, y=80)
regname.place(x=90, y=80)
usrNamelb.place(x=10, y=120)
usrName.place(x=90, y=120)
psswrdlb.place(x=10, y=170)
psswrd.place(x=90, y=170)


showbtn = Button(admin, text="show",width=5, command=show, bd=2)
addb = Button(admin, text="Add", width=5, bd=2, command=add)
removebtn = Button(admin, text="Delete", width=5, bd=2, command=delete)
clearbtn = Button(admin, text="Clear", width=5, bd=2, command=clear)
grantbtn = Button(admin, text="Grant", width=5, bd=2, command=grant)
countbtn = Button(admin, text="Count", width=5, bd=2, command=count)
showbtn.place(x=300, y=100)
addb.place(x=380, y=100)
removebtn.place(x=460, y=100)
clearbtn.place(x=540, y=100)
grantbtn.place(x=620, y=100)
countbtn.place(x=700, y=100)



var = IntVar()
admin_radio = Radiobutton(admin, text="admin", variable=var, value=1, fg="white", bg="black")
admin_radio.place(x=10, y=20)


user_radio = Radiobutton(admin, text="Users", variable=var, value=2, fg="white", bg="black")
user_radio.place(x=100, y=20)


admin.geometry("800x600")
admin.configure(bg="grey")
admin.mainloop()
