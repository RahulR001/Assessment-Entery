from tkinter import *
import tkinter.messagebox
import mysql.connector
from mentor_page import *

db = mysql.connector.connect(
    host='localhost',
    username='root',
    password='rahul125',
    database='shiash_mentors'
)
curser = db.cursor(buffered=True)


def multifun(*functions):
    def fun(*args, **kwargs):
        rtn = None
        for function in functions:
            rtn = function(*args, **kwargs)
    return fun


def mainwin():
    global main
    main = Tk()
    main.title('Authenthication')
    width = 590
    height = 500
    screen_width = main.winfo_screenwidth()
    screen_height = main.winfo_screenheight()
    x = (width)-(screen_width/15)
    y = (height)-(screen_height/3)
    main.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
    main.configure(bg='black')

    Label(main, text='', bg='black').grid(row=0, column=3)

    Label(main, text=' Shiash Info Solutions Private Limited', bg='black', fg='white', font='Roboto 24 bold'
          ).grid(row=1, columnspan=8, )
    Label(main, text='', bg='black').grid(row=2, column=3)
    Label(main, text='                  Assessment Report', bg='black',
          fg='white', font='Roboto 22 bold').grid(row=3, columnspan=6)
    Label(main, text='                    Login to Access your Desk',
          bg='black', fg='green', font='Roboto 18 bold').grid(row=4, columnspan=6)
    Label(main, text='', bg='black').grid(row=5, columnspan=3)
    Button(main, text='Admin Login', font=('Helvetica 15 bold '),
           command=admins, bg='grey', width=12, height=2).place(x=230, y=200)
    Button(main, text='Mentor Login', font=('Helvetica 15 bold '),
           command=mentors, bg='grey',
           width=12, height=2).place(x=230, y=300)
    mainloop()


def mentors():
    global mentor
    mentor = Tk()
    mentor.title('Mentor Login')
    width = 590
    height = 500
    screen_width = mentor.winfo_screenwidth()
    screen_height = mentor.winfo_screenheight()
    x = (width)-(screen_width/15)
    y = (height)-(screen_height/3)
    mentor.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

    mentor.configure(bg='black')
    main.withdraw()
    global user_name
    global password
    user_name = StringVar()
    password = StringVar()
    Label(mentor, text='', bg='black').grid(row=0, column=3)

    Label(mentor, text=' Shiash Info Solutions Private Limited', bg='black', fg='white', font='Roboto 24 bold'
          ).grid(row=1, columnspan=8, )
    Label(mentor, text='', bg='black').grid(row=2, column=3)
    Label(mentor, text='                  Mentor Login', bg='black',
          fg='white', font='Roboto 22 bold').grid(row=3, columnspan=6)
    Label(mentor, text='Username :', bg='black',
          fg='white', font='Roboto 15 bold').place(x=170, y=150)
    Entry(mentor, textvariable=user_name, width=15,
          font='Roboto 22 bold').place(x=170, y=190)
    Label(mentor, text='Password :', bg='black',
          fg='white', font='Roboto 15 bold').place(x=170, y=250)
    Entry(mentor, textvariable=password, width=15,
          font='Roboto 22 bold', show='*').place(x=170, y=290)
    Label(mentor, text="Don't have an account create one", bg='black',
          fg='white', font='Roboto 12 bold').place(x=140, y=350)
    Button(mentor, command=mentor_registration, text='here', font='Roboto 12 bold',
           bg='black', fg='blue', border=0).place(x=400, y=350)
    Label(mentor, text="Not a mentor click", bg='black',
          fg='white', font='Roboto 12 bold').place(x=200, y=380)
    Button(mentor, command=multifun(mentor.withdraw, mainwin), text='here', font='Roboto 12 bold',
           bg='black', fg='blue', border=0).place(x=340, y=380)
    Button(mentor, text='Login', command=multifun(mentor_login, mentor.withdraw), font=('Helvetica 15 bold '),
           bg='green', width=10, height=1).place(x=230, y=415)


def mentor_login():
    username = user_name.get()
    password1 = password.get()
    curser.execute(
        "select * from mentors where user_name=%s and password1=%s ", [username, password1])
    val = curser.fetchone()
    if val != None:
        tkinter.messagebox.showinfo('mentor', 'Asscess Granted')
        mains()
    else:
        tkinter.messagebox.showinfo('mentor', 'Asscess Denied')


def mentor_registration():
    global reg
    reg = Tk()
    reg.title('Registration')
    reg.configure(bg='black')
    width = 590
    height = 700
    screen_width = reg.winfo_screenwidth()
    screen_height = reg.winfo_screenheight()
    x = (width)-(screen_width/15)
    y = (height)-(screen_height/1.4)
    reg.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
    mentor.withdraw()
    Label(reg, text='', bg='black').grid(row=0, column=3)

    Label(reg, text=' Shiash Info Solutions Private Limited', bg='black', fg='white', font='Roboto 24 bold'
          ).grid(row=1, columnspan=8, )
    Label(reg, text='', bg='black').grid(row=2, column=3)
    Label(reg, text='             Mentor Registration', bg='black',
          fg='white', font='Roboto 22 bold').grid(row=3, columnspan=6)
    Label(reg, text='', bg='black').grid(row=4, column=3)
    Label(reg, text='First Name', font='Roboto 13 bold', bg='black',
          fg='white').grid(row=5, column=1, sticky='w')
    Label(reg, text='', bg='black').grid(row=6, column=3)
    Label(reg, text='Last Name', font='Roboto 13 bold', bg='black',
          fg='white').grid(row=7, column=1, sticky='w')
    Label(reg, text='', bg='black').grid(row=8, column=3)
    Label(reg, text='User Name', font='Roboto 13 bold',
          bg='black', fg='white').grid(row=9, column=1, sticky='w')
    Label(reg, text='', bg='black').grid(row=10, column=3)
    Label(reg, text='Email', font='Roboto 13 bold',
          bg='black', fg='white').grid(row=11, column=1, sticky='w')
    Label(reg, text='', bg='black').grid(row=12, column=3)
    Label(reg, text='Password', font='Roboto 13 bold',
          bg='black', fg='white').grid(row=13, column=1, sticky='w')
    Label(reg, text='', bg='black').grid(row=14, column=3)
    Label(reg, text='Retype Password', font='Roboto 13 bold',
          bg='black', fg='white').grid(row=15, column=1, sticky='w')
    Label(reg, text="Already have an account login", bg='black',
          fg='white', font='Roboto 12 bold').place(x=30, y=420)
    Button(reg, command=multifun(mentors, reg.withdraw), text='here', font='Roboto 12 bold',
           bg='black', fg='blue', border=0).place(x=265, y=420)

    global first_name
    global last_name
    global user_name
    global email
    global password1
    global password2
    first_name = StringVar()
    last_name = StringVar()
    user_name = StringVar()
    email = StringVar()
    password1 = StringVar()
    password2 = StringVar()

    Entry(reg, textvariable=first_name, font='Roboto 13 bold').grid(
        row=5, column=2, sticky='w')
    Entry(reg, textvariable=last_name, font='Roboto 13 bold').grid(
        row=7, column=2, sticky='w')
    Entry(reg, textvariable=user_name, font='Roboto 13 bold').grid(
        row=9, column=2, sticky='w')
    Entry(reg, textvariable=email, font='Roboto 13 bold').grid(
        row=11, column=2, sticky='w')
    Entry(reg, textvariable=password1, show='*', font='Roboto 13 bold').grid(
        row=13, column=2, sticky='w')
    Entry(reg, textvariable=password2, show='*', font='Roboto 13 bold').grid(
        row=15, column=2, sticky='w')
    Button(reg, text='Register', font=('Helvetica 15 bold '),
           command=register, bg='green', width=10, height=1).place(x=230, y=460)


def register():

    first1_name = first_name.get()
    last1_name = last_name.get()
    user1_name = user_name.get()
    email1 = email.get()
    password11 = password1.get()
    password21 = password2.get()
    curser.execute("insert into mentors (first_name,last_name,user_name,email,password1,password2 ) values(%s,%s,%s,%s,%s,%s  )", [
                   first1_name, last1_name, user1_name, email1, password11, password21])
    db.commit()
    first1_name = first_name.set('')
    last1_name = last_name.set('')
    user1_name = user_name.set('')
    email1 = email.set('')
    password11 = password1.set('')
    password21 = password2.set('')
    mentor.deiconify()
    reg.withdraw()


def admins():
    global admin
    admin = Tk()
    admin.title('Admin Login')
    width = 590
    height = 500
    screen_width = admin.winfo_screenwidth()
    screen_height = admin.winfo_screenheight()
    x = (width)-(screen_width/15)
    y = (height)-(screen_height/3)
    admin.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

    admin.configure(bg='black')
    main.withdraw()
    Label(admin, text='', bg='black').grid(row=0, column=3)

    Label(admin, text=' Shiash Info Solutions Private Limited', bg='black', fg='white', font='Roboto 24 bold'
          ).grid(row=1, columnspan=8, )
    Label(admin, text='', bg='black').grid(row=2, column=3)
    Label(admin, text='                  Admin Login', bg='black',
          fg='white', font='Roboto 22 bold').grid(row=3, columnspan=6)
    Label(admin, text='Username :', bg='black',
          fg='white', font='Roboto 15 bold').place(x=170, y=150)
    Entry(admin, width=15, font='Roboto 22 bold').place(x=170, y=190)
    Label(admin, text='Password :', bg='black',
          fg='white', font='Roboto 15 bold').place(x=170, y=250)
    Entry(admin, width=15, font='Roboto 22 bold', show='*').place(x=170, y=290)
    Label(admin, text="Not an admin click", bg='black',
          fg='white', font='Roboto 12 bold').place(x=170, y=350)
    Button(admin, command=multifun(admin.withdraw, mainwin), text='here', font='Roboto 12 bold',
           bg='black', fg='blue', border=0).place(x=320, y=350)
    Button(admin, text='Login', font=('Helvetica 15 bold '),
           bg='green', width=10, height=1).place(x=230, y=400)


if __name__ == "__main__":
    mainwin()
