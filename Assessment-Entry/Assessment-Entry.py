from tkinter import *
import tkinter.messagebox
import mysql.connector


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
    mlist = Frame(window, bg='black')
    mlist.pack()
    curser.execute('select * from assessment_data')
    val = curser.fetchall()
    rows = len(val)
    colns = len(val[0])
    Label(mlist, text=' Shiash Info Solutions Private Limited',
          bg='black', fg='white', font='Roboto 34 bold').place(x=97, y=63)
    Label(mlist, text="Assessment Data's", bg='black',
          fg='white', font='Roboto 28 bold').place(x=329, y=143)
    Label(mlist,  bg='black').grid(row=0, column=0)
    Label(mlist,  bg='black').grid(row=1, column=0)
    Label(mlist,  bg='black').grid(row=2, column=0)
    Label(mlist,  bg='black').grid(row=3, column=0)
    Label(mlist,  bg='black').grid(row=4, column=0)
    Label(mlist,  bg='black').grid(row=5, column=0)
    Label(mlist,  bg='black').grid(row=6, column=0)
    Label(mlist,  bg='black').grid(row=7, column=0)
    Label(mlist,  bg='black').grid(row=8, column=0)
    Label(mlist,  bg='black').grid(row=9, column=0)
    Label(mlist,  bg='black').grid(row=10, column=0)
    Label(mlist, text='Intern Id   ', font='Roboto 15 bold',
          bg='black', fg='white').grid(row=15, column=0)
    Label(mlist, text='Intern Name   ', font='Roboto 13 bold',
          bg='black', fg='white').grid(row=15, column=1)
    Label(mlist, text='Assessment - I   ', font='Roboto 13 bold',
          bg='black', fg='white').grid(row=15, column=2)
    Label(mlist, text='Assessment - II   ', font='Roboto 13 bold',
          bg='black', fg='white').grid(row=15, column=3)
    Label(mlist, text='Assessment - III   ', font='Roboto 13 bold',
          bg='black', fg='white').grid(row=15, column=4)
    Label(mlist, text='Total   ', font='Roboto 13 bold',
          bg='black', fg='white').grid(row=15, column=5)
    Label(mlist, text='Percentage   ', font='Roboto 13 bold',
          bg='black', fg='white').grid(row=15, column=6)
    m = 6
    for i in range(rows):
        for j in range(colns):
            s = Entry(mlist, width=16, font='Roboto 13 bold')
            s.grid(row=m+i+10, column=j)
            s.insert(END, val[i][j])
    Button(mlist, text='Go Back', command=multifun(mentors_dashboard, mlist.destroy),
           bg='black', fg='white', font='Helvetica 10 bold ', width=7, height=1).place(x=0, y=10)


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


# ==========logout=========


def logout():
    tkinter.messagebox.showinfo('window', 'Logged Out Successfully')


# ==========home-page=========


def home_page():
    global home
    home = Frame(window, bg='black')
    home.pack()
    Label(home,  bg='black').pack()
    Label(home,  bg='black').pack()
    Label(home,  bg='black').pack()
    Label(home, text='Shiash Info Solutions Private Limited',
          bg='black', fg='white', font='Roboto 34 bold').pack()
    Label(home,  bg='black').pack()
    Label(home, text='Internship Management System', bg='black',
          fg='white', font='Roboto 28 bold').pack()
    Label(home,  bg='black').pack()
    Label(home, text='Login to Access your Desk', bg='black',
          fg='green', font='Roboto 18 bold').pack()
    Label(home,  bg='black').pack()
    Label(home,  bg='black').pack()
    Button(home, text='Admin Login', font=('Helvetica 15 bold '),
           command=admin_frame, bg='grey', width=12, height=2).pack()
    Label(home,  bg='black').pack()
    Label(home,  bg='black').pack()
    Button(home, text='Mentor Login', font=('Helvetica 15 bold '),
           command=mentor_frame, bg='grey', width=12, height=2).place(x=210, y=400)
    Label(home,  bg='black').pack()
    Label(home,  bg='black').pack()
    Button(home, text='Student Login', command=student_frame, font=('Helvetica 15 bold '),
           bg='grey', width=12, height=2).place(x=430, y=400)
    Label(home,  bg='black').pack()
    Label(home,  bg='black').pack()
    Label(home,  bg='black').pack()
    Label(home,  bg='black').pack()
    Label(home,  bg='black').pack()
    Label(home,  bg='black').pack()
    Label(home,  bg='black').pack()
    Label(home,  bg='black').pack()
    Label(home, text='Developed by RAHUL R  SISPLINT : 329191896',
          bg='black', fg='white', font='a 20 bold').pack()
    Label(home,  bg='black').pack()
    Label(home, text='DEVELOPER TRAINEE - INTERN',
          bg='black', fg='white', font='a 16 bold').pack()


# ==========admin-page==========


def admin_frame():
    global admin
    admin = Frame(window, bg='black')
    admin.pack()
    home.destroy()
    global admin_username
    global admin_password
    admin_username = StringVar()
    admin_password = StringVar()
    Label(admin,  bg='black').pack()
    Label(admin,  bg='black').pack()
    Label(admin,  bg='black').pack()
    Label(admin, text='Shiash Info Solutions Private Limited',
          bg='black', fg='white', font='Roboto 34 bold').pack()
    Label(admin,  bg='black').pack()
    Label(admin, text='Admin Login', bg='black',
          fg='white', font='Roboto 28 bold').pack()
    Label(admin,  bg='black').pack()
    Label(admin,  bg='black').pack()
    Label(admin,  bg='black').pack()
    Label(admin,  bg='black').pack()
    Label(admin, text='Username :', bg='black', fg='white',
          font='Roboto 15 bold').place(x=270, y=240)
    Entry(admin, textvariable=admin_username,
          width=15, font='Roboto 22 bold').pack()
    Label(admin,  bg='black').pack()
    Label(admin,  bg='black').pack()
    Label(admin,  bg='black').pack()
    Label(admin, text='Password :', bg='black', fg='white',
          font='Roboto 15 bold').place(x=270, y=340)
    Entry(admin,  width=15, textvariable=admin_password,
          font='Roboto 22 bold', show='*').pack()
    Label(admin,  bg='black').pack()
    Label(admin,  bg='black').pack()
    Label(admin, text="Not an Admin click", bg='black',
          fg='white', font='Roboto 12 bold').place(x=310, y=440)
    Button(admin, text='here', font='Roboto 12 bold', command=multifun(home_page, admin.destroy),
           bg='black', fg='blue', border=0).place(x=460, y=440)
    Label(admin,  bg='black').pack()
    Button(admin, text='Login', command=multifun(admin_dashboard, admin.destroy),  font=('Helvetica 15 bold '),
           bg='green', width=10, height=1).pack()


# ==========admin-login==========


def admin_login():
    username = admin_username.get()
    password = admin_password.get()
    if username == 'admin' and password == 'admin':
        tkinter.messagebox.showinfo('mentor', 'Asscess Granted')
        admin_dashboard()
    else:
        tkinter.messagebox.showinfo('mentor', 'Asscess Denied')
        admin_frame()


# ==========admin-dashboard-page=========


def admin_dashboard():
    admin_dash = Frame(window, bg='black')
    admin_dash.pack()
    Label(admin_dash,  bg='black').pack()
    Label(admin_dash,  bg='black').pack()
    Label(admin_dash,  bg='black').pack()
    Label(admin_dash, text='Shiash Info Solutions Private Limited',
          bg='black', fg='white', font='Roboto 34 bold').pack()
    Label(admin_dash,  bg='black').pack()
    Label(admin_dash, text='Admin Dashboard', bg='black',
          fg='white', font='Roboto 28 bold').pack()
    Label(admin_dash,  bg='black').pack()
    Label(admin_dash,  bg='black').pack()
    Label(admin_dash,  bg='black').pack()
    Label(admin_dash,  bg='black').pack()
    Label(admin_dash,  bg='black').pack()
    Label(admin_dash,  bg='black').pack()
    Label(admin_dash,  bg='black').pack()
    Label(admin_dash,  bg='black').pack()
    Label(admin_dash,  bg='black').pack()
    Label(admin_dash,  bg='black').pack()
    Label(admin_dash,  bg='black').pack()
    Label(admin_dash,  bg='black').pack()
    Label(admin_dash,  bg='black').pack()
    Label(admin_dash,  bg='black').pack()
    Label(admin_dash,  bg='black').pack()
    Label(admin_dash,  bg='black').pack()
    Label(admin_dash,  bg='black').pack()
    Label(admin_dash,  bg='black').pack()
    Button(admin_dash, text="Mentor's Data", font=('Helvetica 15 bold '), command=multifun(mentors_data, admin_dash.destroy),
           bg='grey', width=12, height=2).place(x=320, y=300)
    Button(admin_dash, text="Student's Data",  font=('Helvetica 15 bold '), command=multifun(students_data, admin_dash.destroy),
           bg='grey', width=12, height=2).place(x=320, y=400)
    Button(admin_dash, text="Assessment Data",  font=('Helvetica 13 bold '),
           bg='grey', width=14, height=3).place(x=320, y=500)
    Button(admin_dash, text='Logout', command=multifun(home_page, admin_dash.destroy, logout), bg='black', fg='white', font='Roboto 10 bold',
           width=7, height=1).place(x=730, y=10)


# ==========mentors-data==========


def mentors_data():
    global mentors_details
    mentors_details = Frame(window, bg='black')
    mentors_details.pack()
    curser.execute(
        'select id, first_name, last_name, user_name, email from mentors ')
    val = curser.fetchall()
    rows = len(val)
    colns = len(val[0])
    Label(mentors_details,  bg='black').grid(row=0, column=0)
    Label(mentors_details,  bg='black').grid(row=1, column=0)
    Label(mentors_details,  bg='black').grid(row=2, column=0)
    Label(mentors_details,  bg='black').grid(row=3, column=0)
    Label(mentors_details,  bg='black').grid(row=4, column=0)
    Label(mentors_details,  bg='black').grid(row=5, column=0)
    Label(mentors_details,  bg='black').grid(row=6, column=0)
    Label(mentors_details,  bg='black').grid(row=7, column=0)
    Label(mentors_details,  bg='black').grid(row=8, column=0)
    Label(mentors_details,  bg='black').grid(row=9, column=0)
    Label(mentors_details,  bg='black').grid(row=10, column=0)
    Label(mentors_details, text=' Shiash Info Solutions Private Limited            ',
          bg='black', fg='white', font='Roboto 34 bold').place(x=96, y=63)
    Label(mentors_details, text="Mentor's Data", bg='black',
          fg='white', font='Roboto 28 bold').place(x=340, y=143)
    Label(mentors_details, text="Mentor's Id   ", font='Roboto 15 bold',
          bg='black', fg='white').grid(row=15, column=0, sticky='w')
    Label(mentors_details, text='First Name   ', font='Roboto 15 bold',
          bg='black', fg='white').grid(row=15, column=1, sticky='w')
    Label(mentors_details, text='Last Name   ', font='Roboto 15 bold',
          bg='black', fg='white').grid(row=15, column=2, sticky='w')
    Label(mentors_details, text='User Name   ', font='Roboto 15 bold',
          bg='black', fg='white').grid(row=15, column=3, sticky='w')
    Label(mentors_details, text='Email   ', font='Roboto 15 bold',
          bg='black', fg='white').grid(row=15, column=4, sticky='w')
    for i in range(rows):
        for j in range(colns):
            s = Entry(mentors_details, width=16, font='Roboto 15 bold')
            s.grid(row=i+16, column=j)
            s.insert(END, val[i][j])
        Button(mentors_details, text='Delete Mentor', bg='Red', fg='white', font='Helvetica 10 bold ', command=lambda: delete_mentor(val[i][0]),
               width=13, height=1).grid(row=i+16, column=j+1)
    Button(mentors_details, text='Go Back', command=multifun(admin_dashboard, mentors_details.destroy),
           bg='black', fg='white', font='Helvetica 10 bold ', width=7, height=1).place(x=0, y=10)


# ==========students-data==========


def students_data():
    global students_details
    students_details = Frame(window, bg='black')
    students_details.pack()
    curser.execute(
        'select id, first_name, last_name, user_name,department, email from students ')
    val = curser.fetchall()
    if not val:
        tkinter.messagebox.showinfo('students_details', 'No More Data')
        admin_dashboard()
    else:
        rows = len(val)
        colns = len(val[0])
        Label(students_details,  bg='black').grid(row=0, column=0)
        Label(students_details,  bg='black').grid(row=1, column=0)
        Label(students_details,  bg='black').grid(row=2, column=0)
        Label(students_details,  bg='black').grid(row=3, column=0)
        Label(students_details,  bg='black').grid(row=4, column=0)
        Label(students_details,  bg='black').grid(row=5, column=0)
        Label(students_details,  bg='black').grid(row=6, column=0)
        Label(students_details,  bg='black').grid(row=7, column=0)
        Label(students_details,  bg='black').grid(row=8, column=0)
        Label(students_details,  bg='black').grid(row=9, column=0)
        Label(students_details,  bg='black').grid(row=10, column=0)
        Label(students_details, text=' Shiash Info Solutions Private Limited            ',
              bg='black', fg='white', font='Roboto 34 bold').place(x=186, y=63)
        Label(students_details, text="Student's Data", bg='black',
              fg='white', font='Roboto 28 bold').place(x=432, y=143)
        Label(students_details, text="Students's Id   ", font='Roboto 15 bold',
              bg='black', fg='white').grid(row=15, column=0, sticky='w')
        Label(students_details, text='First Name   ', font='Roboto 15 bold',
              bg='black', fg='white').grid(row=15, column=1, sticky='w')
        Label(students_details, text='Last Name   ', font='Roboto 15 bold',
              bg='black', fg='white').grid(row=15, column=2, sticky='w')
        Label(students_details, text='User Name   ', font='Roboto 15 bold',
              bg='black', fg='white').grid(row=15, column=3, sticky='w')
        Label(students_details, text='Department   ', font='Roboto 15 bold',
              bg='black', fg='white').grid(row=15, column=4, sticky='w')
        Label(students_details, text='Email   ', font='Roboto 15 bold',
              bg='black', fg='white').grid(row=15, column=5, sticky='w')
        for i in range(rows):
            for j in range(colns):
                s = Entry(students_details, width=16, font='Roboto 15 bold')
                s.grid(row=i+16, column=j)
                s.insert(END, val[i][j])
            Button(students_details, text='Delete Student', bg='Red', fg='white', font='Helvetica 10 bold ', command=lambda: delete_student(val[i][0]),
                   width=13, height=1).grid(row=i+16, column=j+1)
        Button(students_details, text='Go Back', command=multifun(admin_dashboard, students_details.destroy),
               bg='black', fg='white', font='Helvetica 10 bold ', width=7, height=1).place(x=0, y=10)


# ==========delete-mentor==========


def delete_mentor(id):
    curser.execute('delete from mentors where id=%s', [id])
    db.commit()
    tkinter.messagebox.showinfo(
        'mentors_details', 'Mentor Deleted Successfully')
    mentor_details.destroy()
    mentors_data()


# ==========delete-student==========


def delete_student(id):
    curser.execute('delete from students where id=%s', [id])
    db.commit()
    tkinter.messagebox.showinfo(
        'student_details', 'Student Deleted Successfully')
    students_details.destroy()
    students_data()


# ==========mentors-login-page==========


def mentor_frame():
    global mentor
    mentor = Frame(window, bg='black')
    mentor.pack()
    home.destroy()
    global mentor_username
    global mentor_password
    mentor_username = StringVar()
    mentor_password = StringVar()
    Label(mentor,  bg='black').pack()
    Label(mentor,  bg='black').pack()
    Label(mentor,  bg='black').pack()
    Label(mentor, text='Shiash Info Solutions Private Limited',
          bg='black', fg='white', font='Roboto 34 bold').pack()
    Label(mentor,  bg='black').pack()
    Label(mentor, text='Mentor Login', bg='black',
          fg='white', font='Roboto 28 bold').pack()
    Label(mentor,  bg='black').pack()
    Label(mentor,  bg='black').pack()
    Label(mentor,  bg='black').pack()
    Label(mentor,  bg='black').pack()
    Label(mentor, text='Username :', bg='black', fg='white',
          font='Roboto 15 bold').place(x=270, y=240)
    Entry(mentor, textvariable=mentor_username,
          width=15, font='Roboto 22 bold').pack()
    Label(mentor,  bg='black').pack()
    Label(mentor,  bg='black').pack()
    Label(mentor,  bg='black').pack()
    Label(mentor, text='Password :', bg='black', fg='white',
          font='Roboto 15 bold').place(x=270, y=340)
    Entry(mentor, textvariable=mentor_password, width=15,
          font='Roboto 22 bold', show='*').pack()
    Label(mentor,  bg='black').pack()
    Label(mentor,  bg='black').pack()
    Label(mentor,  bg='black').pack()
    Label(mentor,  bg='black').pack()
    Label(mentor,  bg='black').pack()
    Label(mentor, text="Don't have an account create one", bg='black',
          fg='white', font='Roboto 12 bold').place(x=240, y=440)
    Button(mentor, command=multifun(mentor_registration, mentor.destroy), text='here',
           font='Roboto 12 bold', bg='black', fg='blue', border=0).place(x=500, y=440)
    Label(mentor, text="Not a Mentor click", bg='black',
          fg='white', font='Roboto 12 bold').place(x=290, y=480)
    Button(mentor, text='here', font='Roboto 12 bold', command=multifun(home_page, mentor.destroy),
           bg='black', fg='blue', border=0).place(x=440, y=480)
    Button(mentor, text='Login',  font=('Helvetica 15 bold '),
           command=multifun(mentor_login, mentor.destroy), bg='green', width=10, height=1).pack()


# ==========mentors-registration-page==========


def mentor_registration():
    global mentor_reg
    mentor_reg = Frame(window, bg='black')
    mentor_reg.pack()
    Label(mentor_reg,  bg='black').pack()
    Label(mentor_reg,  bg='black').pack()
    Label(mentor_reg,  bg='black').pack()
    Label(mentor_reg, text='Shiash Info Solutions Private Limited',
          bg='black', fg='white', font='Roboto 34 bold').pack()
    Label(mentor_reg,  bg='black').pack()
    Label(mentor_reg, text="Mentor's Registration", bg='black',
          fg='white', font='Roboto 28 bold').pack()
    Label(mentor_reg,  bg='black').pack()
    Label(mentor_reg,  bg='black').pack()
    Label(mentor_reg,  bg='black').pack()
    Label(mentor_reg,  bg='black').pack()
    Label(mentor_reg,  bg='black').pack()
    Label(mentor_reg,  bg='black').pack()
    Label(mentor_reg,  bg='black').pack()
    Label(mentor_reg,  bg='black').pack()
    Label(mentor_reg,  bg='black').pack()
    Label(mentor_reg,  bg='black').pack()
    Label(mentor_reg,  bg='black').pack()
    Label(mentor_reg,  bg='black').pack()
    Label(mentor_reg,  bg='black').pack()
    Label(mentor_reg,  bg='black').pack()
    Label(mentor_reg,  bg='black').pack()
    Label(mentor_reg, text='First Name :', font='Roboto 18 bold',
          bg='black', fg='white').place(x=150, y=230)
    Label(mentor_reg,  bg='black').pack()
    Label(mentor_reg, text='Last Name :', font='Roboto 18 bold',
          bg='black', fg='white').place(x=150, y=280)
    Label(mentor_reg,  bg='black').pack()
    Label(mentor_reg, text='User Name :', font='Roboto 18 bold',
          bg='black', fg='white').place(x=150, y=330)
    Label(mentor_reg,  bg='black').pack()
    Label(mentor_reg, text='Email :', font='Roboto 18 bold',
          bg='black', fg='white').place(x=150, y=380)
    Label(mentor_reg,  bg='black').pack()
    Label(mentor_reg, text='Password :', font='Roboto 18 bold',
          bg='black', fg='white').place(x=150, y=430)
    Label(mentor_reg,  bg='black').pack()
    Label(mentor_reg, text='Retype Password :', font='Roboto 18 bold',
          bg='black', fg='white').place(x=150, y=480)
    Label(mentor_reg, text="Already have an account login", bg='black',
          fg='white', font='Roboto 12 bold').place(x=210, y=530)
    Button(mentor_reg,  text='here', font='Roboto 12 bold', command=multifun(mentor_frame, mentor_reg.destroy),
           bg='black', fg='blue', border=0).place(x=450, y=530)
    global mentor_firstname
    global mentor_lastname
    global mentor_username
    global mentor_email
    global mentor_password1
    global mentor_password2
    mentor_firstname = StringVar()
    mentor_lastname = StringVar()
    mentor_username = StringVar()
    mentor_email = StringVar()
    mentor_password1 = StringVar()
    mentor_password2 = StringVar()
    Entry(mentor_reg, textvariable=mentor_firstname, width=20,
          font='Roboto 13 bold').place(x=430, y=235)
    Entry(mentor_reg, textvariable=mentor_lastname,
          font='Roboto 13 bold').place(x=430, y=280)
    Entry(mentor_reg, textvariable=mentor_username,
          font='Roboto 13 bold').place(x=430, y=330)
    Entry(mentor_reg, textvariable=mentor_email,
          font='Roboto 13 bold').place(x=430, y=380)
    Entry(mentor_reg, textvariable=mentor_password1, show='*',
          font='Roboto 13 bold').place(x=430, y=430)
    Entry(mentor_reg, textvariable=mentor_password2, show='*',
          font='Roboto 13 bold').place(x=430, y=480)
    Button(mentor_reg, text='Register', command=multifun(mentor_register, mentor_reg.destroy, mentor_frame), font=('Helvetica 15 bold '),
           bg='green', width=10, height=1).place(x=310, y=570)


# ==========mentors-registration==========


def mentor_register():
    first_name = mentor_firstname.get()
    last_name = mentor_lastname.get()
    user_name = mentor_username.get()
    email = mentor_email.get()
    password1 = mentor_password1.get()
    password2 = mentor_password2.get()
    curser.execute("insert into mentors (first_name,last_name,user_name,email,password1,password2 ) values(%s,%s,%s,%s,%s,%s  )", [
                   first_name, last_name, user_name, email, password1, password2])
    db.commit()
    tkinter.messagebox.showinfo('window', 'Registered Successfully')


# ==========mentors-login==========


def mentor_login():
    username = mentor_username.get()
    password1 = mentor_password.get()
    curser.execute(
        "select * from mentors where user_name=%s and password1=%s ", [username, password1])
    val = curser.fetchone()
    if val != None:
        tkinter.messagebox.showinfo('mentor', 'Asscess Granted')
        mentors_dashboard()
    else:
        tkinter.messagebox.showinfo('mentor', 'Asscess Denied')
        mentor_frame()


# ==========mentors-dashboard-page=========


def mentors_dashboard():
    mentor_dash = Frame(window, bg='black')
    mentor_dash.pack()
    Label(mentor_dash,  bg='black').pack()
    Label(mentor_dash,  bg='black').pack()
    Label(mentor_dash,  bg='black').pack()
    Label(mentor_dash, text=' Shiash Info Solutions Private Limited    ',
          bg='black', fg='white', font='Roboto 34 bold').pack()
    Label(mentor_dash,  bg='black').pack()
    Label(mentor_dash, text='Assessment MarkEntry', bg='black',
          fg='white', font='Roboto 28 bold').pack()
    Label(mentor_dash,  bg='black').pack()
    Label(mentor_dash,  bg='black').pack()
    Label(mentor_dash,  bg='black').pack()
    Label(mentor_dash,  bg='black').pack()
    Label(mentor_dash,  bg='black').pack()
    Label(mentor_dash,  bg='black').pack()
    Label(mentor_dash,  bg='black').pack()
    Label(mentor_dash,  bg='black').pack()
    Label(mentor_dash,  bg='black').pack()
    Label(mentor_dash,  bg='black').pack()
    Label(mentor_dash,  bg='black').pack()
    Label(mentor_dash,  bg='black').pack()
    Label(mentor_dash,  bg='black').pack()
    Label(mentor_dash,  bg='black').pack()
    Label(mentor_dash,  bg='black').pack()
    Label(mentor_dash, text='Intern Id :', font='Roboto 18 bold',
          bg='black', fg='white').place(x=10, y=230)
    Label(mentor_dash,  bg='black').pack()
    Label(mentor_dash, text='Intern Name :', font='Roboto 18 bold',
          bg='black', fg='white').place(x=10, y=280)
    Label(mentor_dash,  bg='black').pack()
    Label(mentor_dash, text='Assessment - I :', font='Roboto 18 bold',
          bg='black', fg='white').place(x=10, y=330)
    Label(mentor_dash,  bg='black').pack()
    Label(mentor_dash, text='Assessment - II :', font='Roboto 18 bold',
          bg='black', fg='white').place(x=10, y=380)
    Label(mentor_dash,  bg='black').pack()
    Label(mentor_dash, text='Assessment - III :', font='Roboto 18 bold',
          bg='black', fg='white').place(x=10, y=430)
    Label(mentor_dash,  bg='black').pack()
    Label(mentor_dash, text='Total :', font='Roboto 18 bold',
          bg='black', fg='white').place(x=10, y=480)
    Label(mentor_dash,  bg='black').pack()
    Label(mentor_dash, text='Percentage :', font='Roboto 18 bold',
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
    Entry(mentor_dash, textvariable=intern_id, width=25,
          font='Roboto 13 bold').place(x=330, y=235)
    Entry(mentor_dash, textvariable=intern_name, width=25,
          font='Roboto 13 bold').place(x=330, y=280)
    Entry(mentor_dash, textvariable=intern_ass1, width=25,
          font='Roboto 13 bold').place(x=330, y=330)
    Entry(mentor_dash,  textvariable=intern_ass2, width=25,
          font='Roboto 13 bold').place(x=330, y=380)
    Entry(mentor_dash,  textvariable=intern_ass3, width=25,
          font='Roboto 13 bold').place(x=330, y=430)
    Entry(mentor_dash, textvariable=intern_total, width=25,
          font='Roboto 13 bold').place(x=330, y=480)
    Entry(mentor_dash, textvariable=intern_per, width=25,
          font='Roboto 13 bold').place(x=330, y=530)
    Button(mentor_dash, text='ADD', command=add,  bg='green', font='Roboto 15 bold',
           width=7, height=1).place(x=630, y=235)
    Button(mentor_dash, text='VIEW', command=view,   bg='yellow', font='Roboto 15 bold',
           width=7, height=1).place(x=750, y=235)
    Button(mentor_dash, text='UPDATE', command=update,  bg='aqua', font='Roboto 15 bold',
           width=7, height=1).place(x=630, y=300)
    Button(mentor_dash, text='DELETE', command=delete,   bg='red', font='Roboto 15 bold',
           width=7, height=1).place(x=750, y=300)
    Button(mentor_dash, text='CLEAR', command=clear,   bg='grey', font='Roboto 15 bold',
           width=7, height=1).place(x=630, y=370)
    Button(mentor_dash, text='VIEW ALL', command=multifun(viewall, mentor_dash.destroy),   bg='Tan', font='Roboto 15 bold',
           width=7, height=1).place(x=750, y=370)
    Button(mentor_dash, text='TOTAL', command=total,  bg='Purple', font='Roboto 15 bold',
           width=7, height=1).place(x=630, y=440)
    Button(mentor_dash, text='PERCENT', command=percent,   bg='pink', font='Roboto 14 bold',
           width=7, height=1).place(x=750, y=440)
    Button(mentor_dash, text='Logout', command=multifun(home_page, mentor_dash.destroy, logout), bg='black', fg='white', font='Roboto 10 bold',
           width=7, height=1).place(x=795, y=10)


# ==========students-login-page==========


def student_frame():
    global student
    student = Frame(window, bg='black')
    student.pack()
    home.destroy()
    global student_username
    global student_password
    student_username = StringVar()
    student_password = StringVar()
    Label(student,  bg='black').pack()
    Label(student,  bg='black').pack()
    Label(student,  bg='black').pack()
    Label(student, text='Shiash Info Solutions Private Limited',
          bg='black', fg='white', font='Roboto 34 bold').pack()
    Label(student,  bg='black').pack()
    Label(student, text='Student Login', bg='black',
          fg='white', font='Roboto 28 bold').pack()
    Label(student,  bg='black').pack()
    Label(student,  bg='black').pack()
    Label(student,  bg='black').pack()
    Label(student,  bg='black').pack()
    Label(student, text='Username :', bg='black', fg='white',
          font='Roboto 15 bold').place(x=270, y=240)
    Entry(student, textvariable=student_username,
          width=15, font='Roboto 22 bold').pack()
    Label(student, bg='black').pack()
    Label(student, bg='black').pack()
    Label(student, bg='black').pack()
    Label(student, text='Password :', bg='black', fg='white',
          font='Roboto 15 bold').place(x=270, y=340)
    Entry(student, textvariable=student_password, width=15,
          font='Roboto 22 bold', show='*').pack()
    Label(student, bg='black').pack()
    Label(student, bg='black').pack()
    Label(student, bg='black').pack()
    Label(student, bg='black').pack()
    Label(student, bg='black').pack()
    Label(student, text="New Student Register", bg='black',
          fg='white', font='Roboto 12 bold').place(x=290, y=440)
    Button(student, command=multifun(student_registration, student.destroy), text='here',
           font='Roboto 12 bold', bg='black', fg='blue', border=0).place(x=460, y=440)
    Label(student, text="Not a Student click", bg='black',
          fg='white', font='Roboto 12 bold').place(x=300, y=480)
    Button(student, text='here', font='Roboto 12 bold', command=multifun(home_page, student.destroy),
           bg='black', fg='blue', border=0).place(x=450, y=480)

    Button(student, text='Login',  font=('Helvetica 15 bold '),
           command=multifun(student_login, student.destroy), bg='green', width=10, height=1).pack()


# ==========students-registration-page==========


def student_registration():
    global student_reg
    student_reg = Frame(window, bg='black')
    student_reg.pack()
    Label(student_reg,  bg='black').pack()
    Label(student_reg,  bg='black').pack()
    Label(student_reg,  bg='black').pack()
    Label(student_reg, text='Shiash Info Solutions Private Limited',
          bg='black', fg='white', font='Roboto 34 bold').pack()
    Label(student_reg,  bg='black').pack()

    Label(student_reg, text="Student's Registration", bg='black',
          fg='white', font='Roboto 28 bold').pack()
    Label(student_reg,  bg='black').pack()
    Label(student_reg,  bg='black').pack()
    Label(student_reg,  bg='black').pack()
    Label(student_reg,  bg='black').pack()
    Label(student_reg,  bg='black').pack()
    Label(student_reg,  bg='black').pack()
    Label(student_reg,  bg='black').pack()
    Label(student_reg,  bg='black').pack()
    Label(student_reg,  bg='black').pack()
    Label(student_reg,  bg='black').pack()
    Label(student_reg,  bg='black').pack()
    Label(student_reg,  bg='black').pack()
    Label(student_reg,  bg='black').pack()
    Label(student_reg,  bg='black').pack()
    Label(student_reg,  bg='black').pack()
    Label(student_reg,  bg='black').pack()
    Label(student_reg,  bg='black').pack()
    Label(student_reg,  bg='black').pack()
    Label(student_reg, text='First Name :', font='Roboto 18 bold',
          bg='black', fg='white').place(x=150, y=230)
    Label(student_reg,  bg='black').pack()
    Label(student_reg, text='Last Name :', font='Roboto 18 bold',
          bg='black', fg='white').place(x=150, y=280)
    Label(student_reg,  bg='black').pack()
    Label(student_reg, text='User Name :', font='Roboto 18 bold',
          bg='black', fg='white').place(x=150, y=330)
    Label(student_reg,  bg='black').pack()
    Label(student_reg, text='Email :', font='Roboto 18 bold',
          bg='black', fg='white').place(x=150, y=380)
    Label(student_reg, text='Department :', font='Roboto 18 bold',
          bg='black', fg='white').place(x=150, y=430)
    Label(student_reg,  bg='black').pack()
    Label(student_reg, text='Password :', font='Roboto 18 bold',
          bg='black', fg='white').place(x=150, y=480)
    Label(student_reg,  bg='black').pack()
    Label(student_reg, text='Retype Password :', font='Roboto 18 bold',
          bg='black', fg='white').place(x=150, y=530)
    Label(student_reg, text="Already have an account login", bg='black',
          fg='white', font='Roboto 12 bold').place(x=210, y=580)
    Button(student_reg,  text='here', font='Roboto 12 bold', command=multifun(student_reg.destroy, student_frame),
           bg='black', fg='blue', border=0).place(x=450, y=580)
    global student_firstname
    global student_lastname
    global student_username
    global student_email
    global student_department
    global student_password1
    global student_password2
    student_firstname = StringVar()
    student_lastname = StringVar()
    student_username = StringVar()
    student_email = StringVar()
    student_department = StringVar()
    student_password1 = StringVar()
    student_password2 = StringVar()
    Entry(student_reg, textvariable=student_firstname, width=20,
          font='Roboto 13 bold').place(x=430, y=235)
    Entry(student_reg, textvariable=student_lastname,
          font='Roboto 13 bold').place(x=430, y=280)
    Entry(student_reg, textvariable=student_username,
          font='Roboto 13 bold').place(x=430, y=330)
    Entry(student_reg, textvariable=student_email,
          font='Roboto 13 bold').place(x=430, y=380)
    Entry(student_reg, textvariable=student_department,
          font='Roboto 13 bold').place(x=430, y=430)
    Entry(student_reg, textvariable=student_password1, show='*',
          font='Roboto 13 bold').place(x=430, y=480)
    Entry(student_reg, textvariable=student_password2, show='*',
          font='Roboto 13 bold').place(x=430, y=530)
    Button(student_reg, text='Register', font=('Helvetica 15 bold '), command=multifun(student_register, student_reg.destroy, student_frame),
           bg='green', width=10, height=1).place(x=310, y=630)


# ==========student-registration==========


def student_register():
    first_name = student_firstname.get()
    last_name = student_lastname.get()
    user_name = student_username.get()
    email = student_email.get()
    department = student_department.get()
    password1 = student_password1.get()
    password2 = student_password2.get()
    curser.execute("insert into students (first_name,last_name,user_name,email,password1,password2,department ) values(%s,%s,%s,%s,%s,%s,%s )", [
                   first_name, last_name, user_name, email, password1, password2, department])
    db.commit()
    tkinter.messagebox.showinfo('window', 'Registered Successfully')


# ==========students-login==========


def student_login():
    username = student_username.get()
    password1 = student_password.get()
    curser.execute(
        "select * from students where user_name=%s and password1=%s ", [username, password1])
    val = curser.fetchone()
    if val != None:
        tkinter.messagebox.showinfo('student', 'Asscess Granted')
        # mentors_dashboard()
    else:
        tkinter.messagebox.showinfo('students', 'Asscess Denied')
        student_frame()


# ==========students-dashboard-page=========


def student_dashboard():
    student_dash = Frame(window, bg='black')
    student_dash.pack()
    Label(student_dash,  bg='black').pack()
    Label(student_dash,  bg='black').pack()
    Label(student_dash,  bg='black').pack()
    Label(student_dash, text=' Shiash Info Solutions Private Limited    ',
          bg='black', fg='white', font='Roboto 34 bold').pack()
    Label(student_dash,  bg='black').pack()
    Label(student_dash, text='Assessment MarkEntry', bg='black',
          fg='white', font='Roboto 28 bold').pack()
    Label(student_dash,  bg='black').pack()
    Label(student_dash,  bg='black').pack()
    Label(student_dash,  bg='black').pack()
    Label(student_dash,  bg='black').pack()
    Button(student_dash, text='Logout', command=multifun(home_page, student_dash.destroy, logout), bg='black', fg='white', font='Roboto 10 bold',
           width=7, height=1).place(x=795, y=10)


# ==========main-window==========


def main_window():
    global window
    window = Tk()
    window.state('zoomed')
    window.configure(bg='black')
    window.title('Assesment-Entry')
    home_page()
    mainloop()


# ==========main-function-execution==========


if __name__ == "__main__":
    main_window()
