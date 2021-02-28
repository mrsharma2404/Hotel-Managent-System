from tkinter import*
from tkinter import messagebox
import mysql.connector
var = ""


def submit():
    con=mysql.connector.connect(host="localhost", user="root", password="", db="project1")
    c=con.cursor()
    c.execute("insert into projecta (full_name, age, phone_no, time, date, days, id_type, id_no, room_type, room) values('"+e1.get()+"','"+e2.get()+"','"+e3.get()+"','"+e4.get()+"','"+e5.get()+"','"+e6.get()+"','"+e7.get()+"','"+e8.get()+"','"+e9.get()+"','"+e10.get()+"')") 
    messagebox.showinfo("validation" , "    Room Alloted   ")
    con.commit()

def Rooms():
    con=mysql.connector.connect(host="localhost", user="root", password="", db="project1")
    c=con.cursor()
    c.execute("select distinct room from projecta order by room asc")
    detail= c.fetchall()
    r = int(c.rowcount)
    #a = r[0]
    room.set(detail)
    rowc.set(r)
    #row1.set(a)
    con.commit()

def clear():
    global var
    ea1.set(var)
    ea2.set(var)
    ea3.set(var)
    ea4.set(var)
    ea5.set(var)
    ea6.set(var)
    ea7.set(var)
    ea8.set(var)
    ea9.set(var)
    ea10.set(var)
    

def exit():
    root.destroy()

def back():
    root.destroy()
    import index
    

    

root=Tk()
root.geometry('1368x720')
root.title("Hotel_Management")
root.config(background="black")
root.attributes('-fullscreen', TRUE)

row1=StringVar()
a=StringVar()
r=StringVar()
rowc=StringVar()
room=StringVar()
detail=StringVar()
ea1=StringVar()
ea2=StringVar()
ea3=StringVar()
ea4=StringVar()
ea5=StringVar()
ea6=StringVar()
ea7=StringVar()
ea8=StringVar()
ea9=StringVar()
ea10=StringVar()

Label(root, text='Check in...', bg='Black', fg='Green', font=('Snap ITC', 36)).place(x=50,y=20)

Label(root, text='Full Name - ', bg='black', fg='white', font=('arial', 18)).place(x=100, y=150)
Label(root, text='Age - ', bg='black', fg='white', font=('arial', 18)).place(x=100, y=190)
Label(root, text='Phone No. - ', bg='black', fg='white', font=('arial', 18)).place(x=100, y=230)
Label(root, text='In Time - ', bg='black', fg='white', font=('arial', 18)).place(x=100, y=270)
Label(root, text='In Date - ', bg='black', fg='white', font=('arial', 18)).place(x=100, y=310)
Label(root, text='Booking Days - ', bg='black', fg='white', font=('arial', 18)).place(x=100, y=350)
Label(root, text='ID Type - ', bg='black', fg='white', font=('arial', 18)).place(x=100, y=390)
Label(root, text='ID No. - ', bg='black', fg='white', font=('arial', 18)).place(x=100, y=430)
Label(root, text='Room Type - ', bg='black', fg='white', font=('arial', 18)).place(x=100, y=470)
Label(root, text='Room No. - ', bg='black', fg='white', font=('arial', 18)).place(x=100, y=510)


e1=Entry(root, width=30, textvariable=ea1)
e1.place(x=305, y=160)
e2=Entry(root, width=30, textvariable=ea2)
e2.place(x=305, y=200)
e3=Entry(root, width=30, textvariable=ea3)
e3.place(x=305, y=240)
e4=Entry(root, width=30, textvariable=ea4)
e4.place(x=305, y=280)
e5=Entry(root, width=30, textvariable=ea5)
e5.place(x=305, y=320)
e6=Entry(root,  width=30, textvariable=ea6)
e6.place(x=305, y=360)
e7=Entry(root,  width=30, textvariable=ea7)
e7.place(x=305, y=400)
e8=Entry(root, width=30, textvariable=ea8)
e8.place(x=305, y=440)
e9=Entry(root, width=30, textvariable=ea9)
e9.place(x=305, y=480)
e10=Entry(root, width=30, textvariable=ea10)
e10.place(x=305, y=520)


bt1 = Button(root,text='Submit', bg='black', fg='Green', font=('arial', 15), height=1, width=14, command=submit).place(x=70, y=610)
bt2 = Button(root, text='Reset', bg='black', fg='red', font=('arial', 15), height=1, width=6, command=clear).place(x=320, y=610)
bt2 = Button(root, text='Menu', bg='black', fg='red', font=('arial', 15), height=1, width=6, command=back).place(x=420, y=610)
bt3 = Button(root, text='Exit', bg='black', fg='red', font=('arial', 15), height=1, width=6, command=exit ).place(x=520, y=610)

bt4 = Button(root, text='check taken rooms', bg='black', fg='pink', font=('arial', 15), height=1, width=20, command=Rooms).place(x=800, y=500)
Label(root, textvariable=room, bg='black', fg='white', font=('arial', 15)).place(x=770, y=570)
Label(root, textvariable=rowc, bg='black', fg='white', font=('arial', 8)).place(x=770, y=620)
#Label(root, textvariable=row1, bg='black', fg='white', font=('arial', 15)).place(x=1000, y=340)

File = PhotoImage(file="dracula10.png")
Label(root, height=350, bg='black', width=550, image=File).place(x=700, y=90)

root.mainloop()