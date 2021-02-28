from tkinter import*

def checkin():
    root.destroy()
    import checkin

def Guestlist():
    root.destroy()
    import allguest   

def checkout():
    root.destroy()
    import checkout

def guest1():
    root.destroy()
    import oneguest

def exit():
    root.destroy()

root=Tk()
root.geometry('1368x720')
root.title("Hotel_Management")
root.config(background="black")
root.attributes('-fullscreen', TRUE)

File = PhotoImage(file='dracula5.png')
Label(root, bg='black', height=500, width=370, image=File).place(x=1, y=150)
#File2 = PhotoImage(file=("devis.png"))
#Label(root, bg='black', height=500, width=370, image=File2).place(x=900, y=150)

Label(root, text="WELCOME TO HOTEL TRANSYLVANIA", bg="black", fg="Red", font=('Snap ITC',42) ).place(x=50, y=50)
bt1 = Button(root, text="        Check in       ", bg='black', fg='White', font=('arial', 18), height=2, width=30, command=checkin).place(x=450, y=200)
bt2 = Button(root, text="   Show Guest List     ", bg='black', fg='White', font=('arial', 18), height=2, width=30, command=Guestlist).place(x=450, y=280)
bt3 = Button(root, text="        Check out      ", bg='black', fg='White', font=('arial', 18), height=2, width=30, command=checkout).place(x=450, y=360)
bt4 = Button(root, text=" Get info of any Guest ", bg='black', fg='White', font=('arial', 18), height=2, width=30, command=guest1).place(x=450, y=440)
bt5 = Button(root, text="          Exit         ", bg='black', fg='White', font=('arial', 18), height=2, width=30, command=exit).place(x=450, y=520)
root.mainloop()