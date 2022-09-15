from tkinter import *
import tkinter.messagebox
import mysql.connector
from mentor_page import *


# ==========database-connectivity==========


db = mysql.connector.connect(
    host='localhost',
    username='root',
    password='rahul125',
    database='shiash_mentors'
)
curser = db.cursor(buffered=True)


# ==========multiple-function-execution==========


def multifun(*functions):
    def fun(*args, **kwargs):
        rtn = None
        for function in functions:
            rtn = function(*args, **kwargs)
    return fun


# ==========function-to-add-data-to-database==========


def add():

    id = intern_id.get()
    name = intern_name.get()
    ass1 = intern_ass1.get()
    ass2 = intern_ass2.get()
    ass3 = intern_ass3.get()
    tot = intern_total.get()
    per = intern_per.get()
    curser.execute('insert into assessment_data values(%s,%s,%s,%s,%s,%s,%s)', [
                   id, name, ass1, ass2, ass3, tot, per])
    db.commit()
    tkinter.messagebox.showinfo('dis', 'Data Added')


# ==========function-to-view-data-from-database==========


def view():

    id = intern_id.get()
    curser.execute('select* from assessment_data where intern_id=%s', [id])
    val = curser.fetchone()
    intern_name.set(val[1])
    intern_ass1.set(val[2])
    intern_ass2.set(val[3])
    intern_ass3.set(val[4])
    intern_total.set(val[5])
    intern_per.set(val[6])


# ==========function-to-updata-data-in-database==========


def update():
    id = intern_id.get()
    name = intern_name.get()
    ass1 = intern_ass1.get()
    ass2 = intern_ass2.get()
    ass3 = intern_ass3.get()
    tot = intern_total.get()
    per = intern_per.get()
    curser.execute('update assessment_data set  intern_name=%s, Assessment_1=%s, Assessment_2=%s, '
                   'Assessment_3=%s, Total=%s, percentage=%s where intern_id=%s ', [name, ass1, ass2, ass3, tot, per, id])
    db.commit()
    tkinter.messagebox.showinfo('dis', 'Data Updated')


# ==========function-to-delete-data-from-database==========


def delete():
    id = intern_id.get()
    curser.execute('delete from assessment_data where intern_id=%s', [id])
    db.commit()
    tkinter.messagebox.showinfo('dis', 'Data Deleted')


# ==========function-to-viewall-data-from-database==========


def viewall():
    global mlist
    mlist = Tk()
    mlist.title('Assessment Report')
    mlist.configure(bg='black')
    mlist.geometry('1036x600')
    curser.execute('select * from assessment_data')
    val = curser.fetchall()
    rows = len(val)
    colns = len(val[0])
    Label(mlist, text='', bg='black').grid(row=0, column=3)

    Label(mlist, text=' Shiash Info Solutions Private Limited', bg='black', fg='white', font='Roboto 24 bold'
          ).grid(row=1, columnspan=8, )
    Label(mlist, text='', bg='black').grid(row=2, column=3)
    Label(mlist, text='        Assessment Report', bg='black',
          fg='white', font='Roboto 18 bold').grid(row=3, columnspan=6)
    Label(mlist, text='', bg='black').grid(row=4, columnspan=3)
    Label(mlist, text='Intern Id   ', font='Roboto 13 bold',
          bg='black', fg='white').grid(row=5, column=0)

    Label(mlist, text='Intern Name   ', font='Roboto 13 bold',
          bg='black', fg='white').grid(row=5, column=1)

    Label(mlist, text='Assessment - I   ', font='Roboto 13 bold',
          bg='black', fg='white').grid(row=5, column=2)

    Label(mlist, text='Assessment - II   ', font='Roboto 13 bold',
          bg='black', fg='white').grid(row=5, column=3)

    Label(mlist, text='Assessment - III   ', font='Roboto 13 bold',
          bg='black', fg='white').grid(row=5, column=4)

    Label(mlist, text='Total   ', font='Roboto 13 bold',
          bg='black', fg='white').grid(row=5, column=5)

    Label(mlist, text='Percentage   ', font='Roboto 13 bold',
          bg='black', fg='white').grid(row=5, column=6)
    m = 6
    for i in range(rows):
        for j in range(colns):
            s = Entry(mlist, width=16, font='Roboto 13 bold')
            s.grid(row=m+i+1, column=j)
            s.insert(END, val[i][j])


# ==========function-to-clear-data-from-entry==========


def clear():

    intern_id.set('')
    intern_name.set('')
    intern_ass1.set('')
    intern_ass2.set('')
    intern_ass3.set('')
    intern_total.set('')
    intern_per.set('')


# ==========function-to-find-total==========


def total():
    intern_total.set(intern_ass1.get() + intern_ass2.get() + intern_ass3.get())


# ==========function-to-find-precentage==========


def percent():
    per = intern_total.get() / 300
    perc = per * 100
    intern_per.set(perc)


# ==========home-page=========


def home_page():
    global home
    home = Frame(window, bg='black')
    home.pack()

    Label(home, text='', bg='black').pack()
    Label(home, text='', bg='black').pack()
    Label(home, text='', bg='black').pack()
    Label(home, text='Shiash Info Solutions Private Limited',
          bg='black', fg='white', font='Roboto 34 bold').pack()
    Label(home, text='', bg='black').pack()
    Label(home, text='Assessment Report', bg='black',
          fg='white', font='Roboto 28 bold').pack()
    Label(home, text='', bg='black').pack()
    Label(home, text='Login to Access your Desk', bg='black',
          fg='green', font='Roboto 18 bold').pack()
    Label(home, text='', bg='black').pack()
    Label(home, text='', bg='black').pack()
    Button(home, text='Admin Login', font=('Helvetica 15 bold '),
           command=admins, bg='grey', width=12, height=2).pack()
    Label(home, text='', bg='black').pack()
    Label(home, text='', bg='black').pack()
    Button(home, text='Mentor Login', font=('Helvetica 15 bold '),
           command=mentor_frame, bg='grey', width=12, height=2).pack()
    Label(home, text='', bg='black').pack()
    Label(home, text='', bg='black').pack()
    Button(home, text='Student Login', font=('Helvetica 15 bold '),
           bg='grey', width=12, height=2).pack()


# ==========mentors-dashboard-page=========


def mentors_dashboard():
    dash = Frame(window, bg='black')
    dash.pack()
    mentor.destroy()
    Label(dash, text='', bg='black').pack()
    Label(dash, text='', bg='black').pack()
    Label(dash, text='', bg='black').pack()
    Label(dash, text=' Shiash Info Solutions Private Limited            ',
          bg='black', fg='white', font='Roboto 34 bold').pack()
    Label(dash, text='', bg='black').pack()
    Label(dash, text='Assessment MarkEntry', bg='black',
          fg='white', font='Roboto 28 bold').pack()
    Label(dash, text='', bg='black').pack()
    Label(dash, text='', bg='black').pack()
    Label(dash, text='', bg='black').pack()
    Label(dash, text='', bg='black').pack()
    Label(dash, text='', bg='black').pack()
    Label(dash, text='', bg='black').pack()
    Label(dash, text='', bg='black').pack()
    Label(dash, text='', bg='black').pack()
    Label(dash, text='', bg='black').pack()
    Label(dash, text='', bg='black').pack()
    Label(dash, text='', bg='black').pack()
    Label(dash, text='', bg='black').pack()
    Label(dash, text='', bg='black').pack()
    Label(dash, text='', bg='black').pack()
    Label(dash, text='', bg='black').pack()
    Label(dash, text='Intern Id :', font='Roboto 18 bold',
          bg='black', fg='white').place(x=10, y=230)
    Label(dash, text='', bg='black').pack()
    Label(dash, text='Intern Name :', font='Roboto 18 bold',
          bg='black', fg='white').place(x=10, y=280)
    Label(dash, text='', bg='black').pack()
    Label(dash, text='Assessment - I :', font='Roboto 18 bold',
          bg='black', fg='white').place(x=10, y=330)
    Label(dash, text='', bg='black').pack()
    Label(dash, text='Assessment - II :', font='Roboto 18 bold',
          bg='black', fg='white').place(x=10, y=380)
    Label(dash, text='', bg='black').pack()
    Label(dash, text='Assessment - III :', font='Roboto 18 bold',
          bg='black', fg='white').place(x=10, y=430)
    Label(dash, text='', bg='black').pack()
    Label(dash, text='Total :', font='Roboto 18 bold',
          bg='black', fg='white').place(x=10, y=480)
    Label(dash, text='', bg='black').pack()
    Label(dash, text='Percentage :', font='Roboto 18 bold',
          bg='black', fg='white').place(x=10, y=530)
    global intern_id
    global intern_name
    global intern_ass1
    global intern_ass2
    global intern_ass3
    global intern_total
    global intern_per
    intern_id = StringVar()
    intern_name = StringVar()
    intern_ass1 = IntVar()
    intern_ass2 = IntVar()
    intern_ass3 = IntVar()
    intern_total = IntVar()
    intern_per = IntVar()
    Entry(dash, textvariable=intern_id, width=25,
          font='Roboto 13 bold').place(x=330, y=235)
    Entry(dash, textvariable=intern_name, width=25,
          font='Roboto 13 bold').place(x=330, y=280)
    Entry(dash, textvariable=intern_ass1, width=25,
          font='Roboto 13 bold').place(x=330, y=330)
    Entry(dash,  textvariable=intern_ass2, width=25,
          font='Roboto 13 bold').place(x=330, y=380)
    Entry(dash,  textvariable=intern_ass3, width=25,
          font='Roboto 13 bold').place(x=330, y=430)
    Entry(dash, textvariable=intern_total, width=25,
          font='Roboto 13 bold').place(x=330, y=480)
    Entry(dash, textvariable=intern_per, width=25,
          font='Roboto 13 bold').place(x=330, y=530)
    Button(dash, text='ADD', command=add,  bg='green', font='Roboto 15 bold',
           width=7, height=1).place(x=630, y=235)
    Button(dash, text='VIEW', command=view,   bg='yellow', font='Roboto 15 bold',
           width=7, height=1).place(x=750, y=235)
    Button(dash, text='UPDATE', command=update,  bg='aqua', font='Roboto 15 bold',
           width=7, height=1).place(x=630, y=300)
    Button(dash, text='DELETE', command=delete,   bg='red', font='Roboto 15 bold',
           width=7, height=1).place(x=750, y=300)
    Button(dash, text='CLEAR', command=clear,   bg='grey', font='Roboto 15 bold',
           width=7, height=1).place(x=630, y=370)
    Button(dash, text='VIEW ALL', command=viewall,   bg='Tan', font='Roboto 15 bold',
           width=7, height=1).place(x=750, y=370)
    Button(dash, text='TOTAL', command=total,  bg='Purple', font='Roboto 15 bold',
           width=7, height=1).place(x=630, y=440)
    Button(dash, text='PERCENT', command=percent,   bg='pink', font='Roboto 14 bold',
           width=7, height=1).place(x=750, y=440)
    Button(dash, text='Logout',   bg='pink', font='Roboto 10 bold',
           width=7, height=1).place(x=900, y=10)


# ==========mentors-login-page==========


def mentor_frame():
    global mentor
    mentor = Frame(window, bg='black')
    mentor.pack()
    home.destroy()
    global user_name
    global password
    user_name = StringVar()
    password = StringVar()
    Label(mentor, text='', bg='black').pack()
    Label(mentor, text='', bg='black').pack()
    Label(mentor, text='', bg='black').pack()
    Label(mentor, text='Shiash Info Solutions Private Limited',
          bg='black', fg='white', font='Roboto 34 bold').pack()
    Label(mentor, text='', bg='black').pack()
    Label(mentor, text='Mentor Login', bg='black',
          fg='white', font='Roboto 28 bold').pack()
    Label(mentor, text='', bg='black').pack()
    Label(mentor, text='', bg='black').pack()
    Label(mentor, text='', bg='black').pack()
    Label(mentor, text='', bg='black').pack()
    Label(mentor, text='Username :', bg='black', fg='white',
          font='Roboto 15 bold').place(x=270, y=240)
    Entry(mentor, textvariable=user_name,
          width=15, font='Roboto 22 bold').pack()
    Label(mentor, text='', bg='black').pack()
    Label(mentor, text='', bg='black').pack()
    Label(mentor, text='', bg='black').pack()
    Label(mentor, text='Password :', bg='black', fg='white',
          font='Roboto 15 bold').place(x=270, y=340)
    Entry(mentor, textvariable=password, width=15,
          font='Roboto 22 bold', show='*').pack()
    Label(mentor, text='', bg='black').pack()
    Label(mentor, text='', bg='black').pack()
    Label(mentor, text="Don't have an account create one", bg='black',
          fg='white', font='Roboto 12 bold').place(x=240, y=440)
    Button(mentor, command=mentor_registration, text='here',
           font='Roboto 12 bold', bg='black', fg='blue', border=0).place(x=500, y=440)
    Label(mentor, text="Not a mentor  click", bg='black',
          fg='white', font='Roboto 12 bold').place(x=290, y=480)
    Button(mentor, text='here', font='Roboto 12 bold', command=multifun(home_page, mentor.destroy),
           bg='black', fg='blue', border=0).place(x=440, y=480)
    Label(mentor, text='', bg='black').pack()
    Label(mentor, text='', bg='black').pack()
    Label(mentor, text='', bg='black').pack()
    Button(mentor, text='Login',  font=('Helvetica 15 bold '),
           command=mentor_login, bg='green', width=10, height=1).pack()


# ==========mentors-login==========


def mentor_login():
    username = user_name.get()
    password1 = password.get()
    curser.execute(
        "select * from mentors where user_name=%s and password1=%s ", [username, password1])
    val = curser.fetchone()
    if val != None:
        tkinter.messagebox.showinfo('mentor', 'Asscess Granted')
        mentors_dashboard()
    else:
        tkinter.messagebox.showinfo('mentor', 'Asscess Denied')
        mentors_dashboard()


# ==========mentors-registration-page==========


def mentor_registration():
    global reg
    reg = Frame(window, bg='black')
    reg.pack()
    mentor.destroy()
    Label(reg, text='', bg='black').pack()
    Label(reg, text='', bg='black').pack()
    Label(reg, text='', bg='black').pack()
    Label(reg, text='Shiash Info Solutions Private Limited',
          bg='black', fg='white', font='Roboto 34 bold').pack()
    Label(reg, text='', bg='black').pack()

    Label(reg, text="Mentor's Registration", bg='black',
          fg='white', font='Roboto 28 bold').pack()
    Label(reg, text='', bg='black').pack()
    Label(reg, text='', bg='black').pack()
    Label(reg, text='', bg='black').pack()
    Label(reg, text='', bg='black').pack()
    Label(reg, text='', bg='black').pack()
    Label(reg, text='', bg='black').pack()
    Label(reg, text='', bg='black').pack()
    Label(reg, text='', bg='black').pack()
    Label(reg, text='', bg='black').pack()
    Label(reg, text='', bg='black').pack()
    Label(reg, text='', bg='black').pack()
    Label(reg, text='', bg='black').pack()
    Label(reg, text='', bg='black').pack()
    Label(reg, text='', bg='black').pack()
    Label(reg, text='', bg='black').pack()
    Label(reg, text='First Name :', font='Roboto 18 bold',
          bg='black', fg='white').place(x=150, y=230)
    Label(reg, text='', bg='black').pack()
    Label(reg, text='Last Name :', font='Roboto 18 bold',
          bg='black', fg='white').place(x=150, y=280)
    Label(reg, text='', bg='black').pack()
    Label(reg, text='User Name :', font='Roboto 18 bold',
          bg='black', fg='white').place(x=150, y=330)
    Label(reg, text='', bg='black').pack()
    Label(reg, text='Email :', font='Roboto 18 bold',
          bg='black', fg='white').place(x=150, y=380)
    Label(reg, text='', bg='black').pack()
    Label(reg, text='Password :', font='Roboto 18 bold',
          bg='black', fg='white').place(x=150, y=430)
    Label(reg, text='', bg='black').pack()
    Label(reg, text='Retype Password :', font='Roboto 18 bold',
          bg='black', fg='white').place(x=150, y=480)
    Label(reg, text="Already have an account login", bg='black',
          fg='white', font='Roboto 12 bold').place(x=210, y=530)
    Button(reg,  text='here', font='Roboto 12 bold', command=multifun(mentor_frame, reg.destroy),
           bg='black', fg='blue', border=0).place(x=450, y=530)
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
    Entry(reg, textvariable=first_name, width=20,
          font='Roboto 13 bold').place(x=430, y=235)
    Entry(reg, textvariable=last_name, font='Roboto 13 bold').place(x=430, y=280)
    Entry(reg, textvariable=user_name, font='Roboto 13 bold').place(x=430, y=330)
    Entry(reg, textvariable=email, font='Roboto 13 bold').place(x=430, y=380)
    Entry(reg, textvariable=password1, show='*',
          font='Roboto 13 bold').place(x=430, y=430)
    Entry(reg, textvariable=password2, show='*',
          font='Roboto 13 bold').place(x=430, y=480)
    Button(reg, text='Register', font=('Helvetica 15 bold '),
           bg='green', width=10, height=1).place(x=310, y=570)


# ==========mentors-registration==========


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


# ==========admin-page==========


def admins():
    global admin
    admin = Frame(window, bg='black')
    admin.pack()
    home.destroy()
    Label(admin, text='', bg='black').pack()
    Label(admin, text='', bg='black').pack()
    Label(admin, text='', bg='black').pack()
    Label(admin, text='Shiash Info Solutions Private Limited',
          bg='black', fg='white', font='Roboto 34 bold').pack()
    Label(admin, text='', bg='black').pack()
    Label(admin, text='Admin Login', bg='black',
          fg='white', font='Roboto 28 bold').pack()
    Label(admin, text='', bg='black').pack()
    Label(admin, text='', bg='black').pack()
    Label(admin, text='', bg='black').pack()
    Label(admin, text='', bg='black').pack()
    Label(admin, text='Username :', bg='black', fg='white',
          font='Roboto 15 bold').place(x=270, y=240)
    Entry(admin,
          width=15, font='Roboto 22 bold').pack()
    Label(admin, text='', bg='black').pack()
    Label(admin, text='', bg='black').pack()
    Label(admin, text='', bg='black').pack()
    Label(admin, text='Password :', bg='black', fg='white',
          font='Roboto 15 bold').place(x=270, y=340)
    Entry(admin,  width=15,
          font='Roboto 22 bold', show='*').pack()
    Label(admin, text='', bg='black').pack()
    Label(admin, text='', bg='black').pack()
    Label(admin, text="Not an Admin click", bg='black',
          fg='white', font='Roboto 12 bold').place(x=310, y=440)
    Button(admin, text='here', font='Roboto 12 bold', command=multifun(home_page, admin.destroy),
           bg='black', fg='blue', border=0).place(x=460, y=440)
    Label(admin, text='', bg='black').pack()
    Button(admin, text='Login',  font=('Helvetica 15 bold '),
           bg='green', width=10, height=1).pack()


# ==========main-window==========


def main_window():
    global window
    window = Tk()
    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)
    window.state('zoomed')
    window.configure(bg='black')
    home_page()
    mainloop()


# ==========main-function-execution==========


if __name__ == "__main__":
    main_window()
