from tkinter import *
import mysql.connector

root=Tk()
root.geometry('1368x720')
root.title("Hotel_management")
root.config(background='black')
root.attributes('-fullscreen', TRUE)

def show():    
    F1= Frame(root, bg='black', relief=GROOVE)
    F1.place(x=130, y=150, width=1208, height=600)

    con=mysql.connector.connect(host="localhost", user="root", password="", db="project1")
    c=con.cursor()
    c.execute("select * from projecta order by full_name asc limit 0,20")
    i=0 
    for student in c: 
        for j in range(len(student)):
            e = Entry(F1, width=16, bg='black', fg='white') 
            e.grid(row=i, column=j) 
            e.insert(END, student[j])
        i=i+1 

def show2():
    F1= Frame(root, bg='black', relief=GROOVE)
    F1.place(x=130, y=150, width=1208, height=600)
    val=e21.get()
    con=mysql.connector.connect(host="localhost", user="root", password="", db="project1")
    c=con.cursor()
    c.execute("select * from projecta where full_name like '"+val+"%' or id_type like '"+val+"%' order by full_name asc limit 0,20")
    i=0 
    for student in c: 
        for j in range(len(student)):
            e = Entry(F1, width=16, bg='black', fg='white') 
            e.grid(row=i, column=j) 
            e.insert(END, student[j])
        i=i+1 

show()

def back():
    root.destroy()
    import index

def exit():
    root.destroy()

e21=Entry(root)
e21.place(x=800, y=75)

Label(root, text='List of All Guest', font=('Snap ITC', 23), bg='black', fg='green').place(x=530,y=10)
bt6 = Button(root, bg='black', fg='pink', text='Menu',command=back, height=1, width=10, font=('arial', 10)).place(x=1160, y=70)
bt7 = Button(root, bg='black', fg='pink', text='Full List', command=show, height=1, width=10, font=('arial', 10)).place(x=1050, y=70)
bt8 = Button(root, bg='black', fg='Red', text='Exit', command=exit, height=1, width=10, font=('arial', 10)).place(x=1270, y=70)
bt9 = Button(root, bg='black', fg='light green', text='Search', command=show2, height=1, width=10, font=('arial', 10)).place(x=940, y=70)

#stupid frame just for boxes of name, age etc
F2= Frame(root, bg='black', bd=2, relief=GROOVE)
F2.place(x=130, y=110, width=100, height=40)
F3= Frame(root, bg='black', bd=2, relief=GROOVE)
F3.place(x=228, y=110, width=102, height=40)
F4= Frame(root, bg='black', bd=2, relief=GROOVE)
F4.place(x=328, y=110, width=102, height=40)
F5= Frame(root, bg='black', bd=2, relief=GROOVE)
F5.place(x=428, y=110, width=102, height=40)
F6= Frame(root, bg='black', bd=2, relief=GROOVE)
F6.place(x=528, y=110, width=102, height=40)
F7= Frame(root, bg='black', bd=2, relief=GROOVE)
F7.place(x=628, y=110, width=102, height=40)
F8= Frame(root, bg='black', bd=2, relief=GROOVE)
F8.place(x=728, y=110, width=102, height=40)
F11= Frame(root, bg='black', bd=2, relief=GROOVE)
F11.place(x=828, y=110, width=102, height=40)
F12= Frame(root, bg='black', bd=2, relief=GROOVE)
F12.place(x=928, y=110, width=102, height=40)
F9= Frame(root, bg='black', bd=2, relief=GROOVE)
F9.place(x=1028, y=110, width=102, height=40)
F10= Frame(root, bg='black', bd=2, relief=GROOVE)
F10.place(x=1128, y=110, width=102, height=40)
F11= Frame(root, bg='black', bd=2, relief=GROOVE)
F11.place(x=1228, y=110, width=102, height=40)

Label(root, text='Name', font=('arial', 13), bg='black', fg='pink').place(x=133,y=118)
Label(root, text='Age', font=('arial', 13), bg='black', fg='pink').place(x=233,y=118)
Label(root, text='Phone No.', font=('arial', 13), bg='black', fg='pink').place(x=333,y=118)
Label(root, text='In Time', font=('arial', 13), bg='black', fg='pink').place(x=433,y=118)
Label(root, text='In Date', font=('arial', 13), bg='black', fg='pink').place(x=533,y=118)
Label(root, text='Days', font=('arial', 13), bg='black', fg='pink').place(x=633,y=118)
Label(root, text='ID Type', font=('arial', 13), bg='black', fg='pink').place(x=733,y=118)
Label(root, text='ID No.', font=('arial', 13), bg='black', fg='pink').place(x=833,y=118)
Label(root, text='Room Type', font=('arial', 13), bg='black', fg='pink').place(x=933,y=118)
Label(root, text='Room No.', font=('arial', 13), bg='black', fg='pink').place(x=1033,y=118)
Label(root, text='Out Time', font=('arial', 13), bg='black', fg='pink').place(x=1133,y=118)
Label(root, text='Out Time', font=('arial', 13), bg='black', fg='pink').place(x=1233,y=118)

File = PhotoImage(file='dracula11.png')
Label(root, image=File, bg='black', height=100, width=200).place(x=1, y=6)
root.mainloop()
