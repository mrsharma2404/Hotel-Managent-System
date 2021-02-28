from tkinter import *
import mysql.connector
global e1
def getdetails():
    con=mysql.connector.connect(host="localhost", user="root", password="", db="project1")
    c=con.cursor()
    c.execute("update projecta set out_time='"+e2.get()+"', out_date='"+e3.get()+"' where full_name='"+e1.get()+"'")

    c.execute("select full_name from projecta where full_name='"+e1.get()+"'")
    detail1 = c.fetchall()
    c.execute("select age from projecta where full_name='"+e1.get()+"'")
    detail2 = c.fetchall()
    c.execute("select phone_no from projecta where full_name='"+e1.get()+"'")
    detail3 = c.fetchall()
    c.execute("select time from projecta where full_name='"+e1.get()+"'")
    detail4 = c.fetchall()
    c.execute("select date from projecta where full_name='"+e1.get()+"'")
    detail5 = c.fetchall()
    c.execute("select days from projecta where full_name='"+e1.get()+"'")
    detail6 = c.fetchall()
    c.execute("select id_type from projecta where full_name='"+e1.get()+"'")
    detail7 = c.fetchall()
    c.execute("select id_no from projecta where full_name='"+e1.get()+"'")
    detail8 = c.fetchall()
    c.execute("select room from projecta where full_name='"+e1.get()+"'")
    detail9 = c.fetchall()
    c.execute("select out_time from projecta where full_name='"+e1.get()+"'")
    detail10 = c.fetchall()
    c.execute("select out_date from projecta where full_name='"+e1.get()+"'")
    detail11 = c.fetchall()
    c.execute("select room_type from projecta where full_name='"+e1.get()+"'")
    detail12 = c.fetchall()
    row1.set(detail1)
    row2.set(detail2)
    row3.set(detail3)
    row4.set(detail4)
    row5.set(detail5)
    row6.set(detail6)
    row7.set(detail7)
    row8.set(detail8)
    row9.set(detail9)
    row10.set(detail10)
    row11.set(detail11)
    row12.set(detail12)
    
    con.commit()

def back():
    root.destroy()
    import index

def exit():
    root.destroy()

def total():
    a = int(e5.get())
    b = int(e6.get())
    c = int(e7.get())
    d = a*b
    e = d*c/100
    t = d-e
    totalcharge.set(t)

def reciept1():
    global row21
    global detail21
    global e1
    
    row21=StringVar()
    detail21=StringVar()
    
    con=mysql.connector.connect(host="localhost", user="root", password="", db="project1")
    c=con.cursor()
    c.execute("select full_name from projecta where full_name='"+e1.get()+"'")
    detail21 = c.fetchall()
    row21.set(detail21)
    con=mysql.connector.connect(host="localhost", user="root", password="", db="project1")
    c=con.cursor()
    c.execute("delete from projecta where full_name='"+e1.get()+"'")
    
    con.commit()
    
    root=Tk()
    root.geometry('800x600')
    root.title('Cash Memo')
    root.config(background='White')

    Label(root, text="INVOICE", fg='black', bg='white', font=('Bahnschrift', 25)).place(x=350, y=30)
    Label(root, text="Hotel Transylvania", fg='black', bg='white', font=('Bahnschrift', 16)).place(x=10, y=10)
    Label(root, text='In the heart of Romania \n surrounded by wild mountains  \n (011)7654321 \n hoteltransylvania@gmail.com', fg='black', bg='white', font=('Bahnschrift', 10)).place(x=10, y=40)
    Label(root, text='Description', bg='white', fg='black', font=('bahnschrift',16)).place(x=180, y=185)
    Label(root, text='Price', bg='white', fg='black', font=('bahnschrift',16)).place(x=510, y=185)
    Label(root, text='Quantity', bg='white', fg='black', font=('bahnschrift',16)).place(x=600, y=185)
    Label(root, text='Total', bg='white', fg='black', font=('bahnschrift',16)).place(x=700, y=185)
    Label(root, textvariable=row21, bg='Black', fg='white', font=('arial', 12), border=2, width=10).place(x=140, y=300)


    Label(root, text=" =======================================================================================", fg='black', bg='white', font=('Bahnschrift', 14)).place(x=1, y=108)
    Label(root, text='________________________________________________________________________________________________________________________________________________________________________________________________________', bg='white', fg='black', font=('bahnschrift',8)).place(x=1, y=210)
    Label(root, text='________________________________________________________________________________________________________________________________________________________________________________________________________', bg='white', fg='black', font=('bahnschrift',8)).place(x=1, y=510)


    root.mainloop()
    
    
    
    

root=Tk()
root.geometry('1368x720')
root.title("Hotel_Management")
root.config(background="black")
root.attributes('-fullscreen', TRUE)

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
row10=StringVar()
detail10=StringVar()
row11=StringVar()
detail11=StringVar()
row12=StringVar()
detail12=StringVar()


intime=StringVar()
outtime=StringVar()
time=StringVar
time1=StringVar()

totalcharge=StringVar()


Label(root, text='Check out...', font=('Snap ITC', 30), bg='black', fg='RED').place(x=30, y=50)
Label(root, text='Enter Name  - ', font=('arial', 16), bg='black', fg='white').place(x=30, y=150)
Label(root, text='Check out time  - ', font=('arial', 16), bg='black', fg='white').place(x=30, y=200)
Label(root, text='Check out date  - ', font=('arial', 16), bg='black', fg='white').place(x=30, y=250)
#Label(root, text='Room No.  - ', font=('arial', 16), bg='black', fg='white').place(x=30, y=300)

e1=Entry(root, width=30)
e1.place(x=200, y=160)
e2=Entry(root, width=30)
e2.place(x=200, y=210)
e3=Entry(root, width=30)
e3.place(x=200, y=260)
#e4=Entry(root, width=30)
#e4.place(x=200, y=310)

bt1= Button(root, text='  Get Detail  ', font=('arial', 14), bg='black', fg='light green', command=getdetails).place(x=30, y=330)
bt2= Button(root, text=' Menu ', font=('arial', 14), bg='black', fg='Red', command=back).place(x=185, y=330)
bt3= Button(root, text=' Exit ', font=('arial', 14), bg='black', fg='Red', command=exit).place(x=270, y=330)

Label(root, textvariable=row1, bg='Black', fg='white', font=('arial', 12), border=2).place(x=140, y=470)
Label(root, textvariable=row2, bg='Black', fg='white', font=('arial', 12), border=2).place(x=140, y=500)
Label(root, textvariable=row3, bg='Black', fg='white', font=('arial', 12), border=2).place(x=140, y=530)
Label(root, textvariable=row7, bg='Black', fg='white', font=('arial', 12), border=2).place(x=140, y=560)
Label(root, textvariable=row8, bg='Black', fg='white', font=('arial', 12), border=2).place(x=140, y=590)
Label(root, textvariable=row9, bg='Black', fg='white', font=('arial', 12), border=2).place(x=140, y=620)
Label(root, textvariable=row4, bg='Black', fg='white', font=('arial', 12), border=2).place(x=500, y=470)
Label(root, textvariable=row5, bg='Black', fg='white', font=('arial', 12), border=2).place(x=500, y=500)
Label(root, textvariable=row6, bg='Black', fg='white', font=('arial', 12), border=2).place(x=500, y=530)
Label(root, textvariable=row10, bg='Black', fg='white', font=('arial', 12), border=2).place(x=500, y=560)
Label(root, textvariable=row11, bg='Black', fg='white', font=('arial', 12), border=2).place(x=500, y=590)
Label(root, textvariable=row12, bg='Black', fg='white', font=('arial', 12), border=2).place(x=140, y=650)


Label(root, text='Name - ', bg='Black', fg='white', font=('arial', 12), border=2).place(x=10, y=470)
Label(root, text='Age - ', bg='Black', fg='white', font=('arial', 12), border=2).place(x=10, y=500)
Label(root, text='Phone No. - ', bg='Black', fg='white', font=('arial', 12), border=2).place(x=10, y=530)
Label(root, text='ID Type - ', bg='Black', fg='white', font=('arial', 12), border=2).place(x=10, y=560)
Label(root, text='ID No. - ', bg='Black', fg='white', font=('arial', 12), border=2).place(x=10, y=590)
Label(root, text='Room No. - ', bg='Black', fg='white', font=('arial', 12), border=2).place(x=10, y=620)
Label(root, text='Room Type. - ', bg='Black', fg='white', font=('arial', 12), border=2).place(x=10, y=650)
Label(root, text='Check in Time - ', bg='Black', fg='white', font=('arial', 12), border=2).place(x=350, y=470)
Label(root, text='Check in Date - ', bg='Black', fg='white', font=('arial', 12), border=2).place(x=350, y=500)
Label(root, text='Booked Days - ', bg='Black', fg='white', font=('arial', 12), border=2).place(x=350, y=530)
Label(root, text='Check out time - ', bg='Black', fg='white', font=('arial', 12), border=2).place(x=350, y=560)
Label(root, text='Check out date - ', bg='Black', fg='white', font=('arial', 12), border=2).place(x=350, y=590)

File = PhotoImage(file=("dracula15.png"))
Label(root, bg='black', height=330, width=600, image=File).place(x=670, y=50)


#intime = int(row2)
#outtime = int(row6)
#time = intime-outtime
#time1.set(time)
#Label(root, textvariable=time1, bg='black', fg='Red', font=('arial', 14)).place(x=970, y=120)

Label(root, text="Total Stay Days   ", bg="black", fg="white", font=('arial', 12)).place(x=670, y=470)
Label(root, text="One Day Room Charge  ", bg="black", fg="white", font=('arial', 12)).place(x=670, y=510)
Label(root, text="Discount          ", bg="black", fg="white", font=('arial', 12)).place(x=670, y=550)
Label(root, textvariable=totalcharge, bg='black', fg='Red', font=('arial', 14)).place(x=870, y=620)

e5=Entry(root)
e5.place(x=870, y=480)
e6=Entry(root)
e6.place(x=870, y=520)
e7=Entry(root)
e7.place(x=870, y=560)

bt4= Button(root, text=' Total ', bg='black', fg='Red', font=('arial',12), command=total).place(x=670, y=620)

bt5= Button(root, text='  Reciept  ', bg='black', fg='light Green', font=('arial',15), height=2, width=15, command=reciept1).place(x=1100, y=520)

#Label(root, textvariable=detail, bg='black', fg='white', font=('arial', 16)).place(x=50, y=500)

root.mainloop()