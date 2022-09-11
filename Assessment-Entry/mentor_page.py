from tkinter import *
import mysql.connector
import tkinter.messagebox


db = mysql.connector.connect(
    host='localhost',
    username='root',
    password='rahul125',
    database='Shiash_Assessment'
)
curser = db.cursor(buffered=True)


def main():
    dis = Tk()

    dis.geometry('810x650')
    dis.configure(bg='black')
    dis.title('Assessment Mark Entry')
    Label(text='', bg='black').grid(row=0, column=3)

    Label(text='            Shiash Info Solutions Private Limited', bg='black', fg='white', font='Roboto 24 bold'
          ).grid(row=1, columnspan=4, )
    Label(text='', bg='black').grid(row=2, column=3)
    Label(text='     Assessment Mark Entry', bg='black',
          fg='white', font='Roboto 18 bold').grid(row=3, column=2)
    Label(text='', bg='black').grid(row=4, column=3)
    Label(text='Intern Id', font='Roboto 13 bold', bg='black',
          fg='white').grid(row=5, column=1, sticky='w')
    Label(text='', bg='black').grid(row=6, column=3)
    Label(text='Intern Name', font='Roboto 13 bold', bg='black',
          fg='white').grid(row=7, column=1, sticky='w')
    Label(text='', bg='black').grid(row=8, column=3)
    Label(text='Assessment - I', font='Roboto 13 bold',
          bg='black', fg='white').grid(row=9, column=1, sticky='w')
    Label(text='', bg='black').grid(row=10, column=3)
    Label(text='Assessment - II', font='Roboto 13 bold',
          bg='black', fg='white').grid(row=11, column=1, sticky='w')
    Label(text='', bg='black').grid(row=12, column=3)
    Label(text='Assessment - III', font='Roboto 13 bold',
          bg='black', fg='white').grid(row=13, column=1, sticky='w')
    Label(text='', bg='black').grid(row=14, column=3)
    Label(text='Total', font='Roboto 13 bold', bg='black',
          fg='white').grid(row=15, column=1, sticky='w')
    Label(text='', bg='black').grid(row=16, column=3)
    Label(text='Percentage', font='Roboto 13 bold', bg='black',
          fg='white').grid(row=17, column=1, sticky='w')
    global inter_id
    global intern_name
    global intern_ass1
    global intern_ass2
    global intern_ass3
    global intern_total
    global intern_per
    intern_id = StringVar()
    Entry(dis, textvariable=intern_id, font='Roboto 13 bold').grid(
        row=5, column=2, sticky='w')
    intern_name = StringVar()
    Entry(dis, textvariable=intern_name, font='Roboto 13 bold').grid(
        row=7, column=2, sticky='w')
    intern_ass1 = IntVar()
    Entry(dis, textvariable=intern_ass1, font='Roboto 13 bold').grid(
        row=9, column=2, sticky='w')
    intern_ass2 = IntVar()
    Entry(dis, textvariable=intern_ass2, font='Roboto 13 bold').grid(
        row=11, column=2, sticky='w')
    intern_ass3 = IntVar()
    Entry(dis, textvariable=intern_ass3, font='Roboto 13 bold').grid(
        row=13, column=2, sticky='w')
    intern_total = IntVar()
    Entry(dis, textvariable=intern_total, font='Roboto 13 bold').grid(
        row=15, column=2, sticky='w')
    intern_per = IntVar()
    Entry(dis, textvariable=intern_per, font='Roboto 13 bold').grid(
        row=17, column=2, sticky='w')

    Button(text='ADD', command=add, bg='green', font='Roboto 13 bold',
           width=7, height=1).grid(row=5, column=3)
    Button(text='VIEW', command=view, bg='yellow', font='Roboto 13 bold', width=7, height=1).grid(row=5,
                                                                                                  column=5)
    Button(text='UPDATE', command=update, bg='aqua', font='Roboto 13 bold', width=7, height=1).grid(row=7,
                                                                                                    column=3)
    Button(text='DELETE', command=delete, bg='red', font='Roboto 13 bold', width=7, height=1).grid(row=7,
                                                                                                   column=5)
    Button(text='CLEAR', command=clear, bg='grey',
           font='Roboto 13 bold', width=7, height=1).grid(row=9, column=3)
    Button(text='VIEW ALL', command=viewall, bg='Tan',
           font='Roboto 13 bold', width=7, height=1).grid(row=9, column=5)
    Button(text='TOTAL', command=total, bg='Purple', font='Roboto 13 bold', width=7, height=1).grid(row=11,
                                                                                                    column=3)
    Button(text='PERCENT', command=percent, bg='pink',
           font='Roboto 12 bold', width=7, height=1).grid(row=11, column=5)
    Label(text=' ', bg='black', fg='white',
          font='a 10 bold').grid(row=18, columnspan=8)
    Label(text=' ', bg='black', fg='white',
          font='a 10 bold').grid(row=19, columnspan=8)
    Label(text=' ', bg='black', fg='white',
          font='a 10 bold').grid(row=20, columnspan=8)
    Label(text='Developed by RAHUL R  SISPLINT : 329191896', bg='black', fg='white', font='a 15 bold').grid(row=21,
                                                                                                            columnspan=8)
    Label(text='DEVELOPER TRAINEE - INTERN', bg='black', fg='white', font='a 15 bold').grid(row=22,
                                                                                            columnspan=8)
    mainloop()

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


def delete():
    id = intern_id.get()
    curser.execute('delete from assessment_data where intern_id=%s', [id])
    db.commit()
    tkinter.messagebox.showinfo('dis', 'Data Deleted')


def viewall():
    global mlist
    mlist = Toplevel(dis)
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


def clear():
    intern_id.set('')
    intern_name.set('')
    intern_ass1.set('')
    intern_ass2.set('')
    intern_ass3.set('')
    intern_total.set('')
    intern_per.set('')


def total():
    intern_total.set(intern_ass1.get() + intern_ass2.get() + intern_ass3.get())


def percent():
    per = intern_total.get() / 300
    perc = per * 100
    intern_per.set(perc)




 
