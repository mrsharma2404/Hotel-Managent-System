from tkinter import *
import mysql.connector

var = ""

def detail():
    con=mysql.connector.connect(host="localhost", user="root", password="", db="project1")
    c=con.cursor()
    c.execute("select full_name from projecta where full_name='"+e9.get()+"'")
    detail1 = c.fetchall()
    c.execute("select age from projecta where full_name='"+e9.get()+"'")
    detail2 = c.fetchall()
    c.execute("select phone_no from projecta where full_name='"+e9.get()+"'")
    detail3 = c.fetchall()
    c.execute("select time from projecta where full_name='"+e9.get()+"'")
    detail4 = c.fetchall()
    c.execute("select date from projecta where full_name='"+e9.get()+"'")
    detail5 = c.fetchall()
    c.execute("select days from projecta where full_name='"+e9.get()+"'")
    detail6 = c.fetchall()
    c.execute("select id_type from projecta where full_name='"+e9.get()+"'")
    detail7 = c.fetchall()
    c.execute("select id_no from projecta where full_name='"+e9.get()+"'")
    detail8 = c.fetchall()
    c.execute("select room from projecta where full_name='"+e9.get()+"'")
    detail9 = c.fetchall()
    row1.set(detail1)
    row2.set(detail2)
    row3.set(detail3)
    row4.set(detail4)
    row5.set(detail5)
    row6.set(detail6)
    row7.set(detail7)
    row8.set(detail8)
    row9.set(detail9)
    con.commit()

def clear():
    global var
    ea1.set(var)

def exit():
    root.destroy()

def back():
    root.destroy()
    import index

root=Tk()
root.geometry('1368x720')
root.title("Hotel_management")
root.config(background='black')
root.attributes('-fullscreen', TRUE)
#root.createCanvasImage()

row1=StringVar()
detail1=StringVar()
row2=StringVar()
detail2=StringVar()
row3=StringVar()
detail3=StringVar()
row4=StringVar()
detail4=StringVar()
row5=StringVar()
detail5=StringVar()
row6=StringVar()
detail6=StringVar()
row7=StringVar()
detail7=StringVar()
row8=StringVar()
detail8=StringVar()
row9=StringVar()
detail9=StringVar()
ea1=StringVar()
File=StringVar()

#canvas = Canvas(root, bg='white', height=100, width=50)
#canvas.place(x=600, y=10)
#img = Image.open('index.jpg')
#canvas.image = ImageTk.PhotoImage(img)
#canvas.create_image(0,0, image = canvas.image)

File = PhotoImage(file="dracula23.png")
Label(root, height=350, bg='black', width=550, image=File).place(x=650, y=130)

Label(root, text="Get the Info....", bg='black', fg='pink', font=('Snap ITC',29)).place(x=50, y=30)
Label(root, text="Enter the name - ", bg='black', fg='white', font=('arial', 18)).place(x=50, y=150)

e9=Entry(root, textvariable=ea1, width=25)
e9.place(x=250, y=160)

bt9 = Button(root, text='  Search   ', command=detail, bg='black', fg='light green', font=('arial', 14)).place(x=50, y=230)
bt10 = Button(root, text='Reset',width=6, command=clear, bg='black', fg='pink', font=('arial', 14)).place(x=170, y=230)
bt11 = Button(root, text='Menu', width=6, command=back, bg='black', fg='pink', font=('arial', 14)).place(x=255, y=230)
bt12 = Button(root, text='Exit', width=6, command=exit, bg='black', fg='Red', font=('arial', 14)).place(x=340, y=230)

Label(root, textvariable=row1, bg='Black', fg='white', font=('arial', 12), border=2).place(x=220, y=300)
Label(root, textvariable=row2, bg='Black', fg='white', font=('arial', 12), border=2).place(x=220, y=330)
Label(root, textvariable=row3, bg='Black', fg='white', font=('arial', 12), border=2).place(x=220, y=360)
Label(root, textvariable=row4, bg='Black', fg='white', font=('arial', 12), border=2).place(x=220, y=390)
Label(root, textvariable=row5, bg='Black', fg='white', font=('arial', 12), border=2).place(x=220, y=420)
Label(root, textvariable=row6, bg='Black', fg='white', font=('arial', 12), border=2).place(x=220, y=450)
Label(root, textvariable=row7, bg='Black', fg='white', font=('arial', 12), border=2).place(x=220, y=480)
Label(root, textvariable=row8, bg='Black', fg='white', font=('arial', 12), border=2).place(x=220, y=510)
Label(root, textvariable=row9, bg='Black', fg='white', font=('arial', 12), border=2).place(x=220, y=540)

Label(root, text='Name      - ', bg='Black', fg='white', font=('arial', 12), border=2).place(x=50, y=300)
Label(root, text='Age       - ', bg='Black', fg='white', font=('arial', 12), border=2).place(x=50, y=330)
Label(root, text='Phone No. - ', bg='Black', fg='white', font=('arial', 12), border=2).place(x=50, y=360)
Label(root, text='Check in Time - ', bg='Black', fg='white', font=('arial', 12), border=2).place(x=50, y=390)
Label(root, text='Check in Date - ', bg='Black', fg='white', font=('arial', 12), border=2).place(x=50, y=420)
Label(root, text='Booked Days   - ', bg='Black', fg='white', font=('arial', 12), border=2).place(x=50, y=450)
Label(root, text='ID Type   - ', bg='Black', fg='white', font=('arial', 12), border=2).place(x=50, y=480)
Label(root, text='ID No.    - ', bg='Black', fg='white', font=('arial', 12), border=2).place(x=50, y=510)
Label(root, text='Room No.  - ', bg='Black', fg='white', font=('arial', 12), border=2).place(x=50, y=540)

#canvas=canvas(root, width=300, hieght=300)
#canvas.place(x=500)
#img= ImageTk.photoimage(Image.open("index.jpg"))
#canvas.create_image(10,10 , ANCHOR=NE, Image=img)


root.mainloop()

