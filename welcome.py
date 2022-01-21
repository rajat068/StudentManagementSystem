from tkinter import *
from PIL import Image,ImageTk
import random
import pymysql
from tkinter import messagebox

color = ["blue", "red"]



class welcome:


    def __init__(self,root):
        self.root=root
        self.root.config(bg="white")
        self.root.title("Registration Window")
        self.root.geometry("1350x720+50+10")
        #-----------------bg image--------------------------
        self.bg=ImageTk.PhotoImage(file="4444.jpg")
        bg=Label(self.root,image=self.bg,bg="blue")
        bg.place(x=125,y=0,relwidth=1,relheight=1)
        #--------------------corner bg---------------------------------
        self.cor=ImageTk.PhotoImage(file="images (1).jpg")
        cor=Label(self.root,image=self.cor,bg="red")
        cor.place(x=30,y=10,width=200,height=700)

        def teach():
            fg = random.choice(color)
            faculty.config(fg=fg)
            faculty.after(20, teach)


        faculty = Button(self.root, text="Faculty Login", font=("times", 30, "italic bold"), cursor="hand2",
                         borderwidth=8,bg="yellowgreen",activebackground="blue",command=self.login)
        faculty.place(x=340,y=115)
        teach()

        def stud():
            fg = random.choice(color)
            student.config(fg=fg)
            student.after(20, stud)


        student = Button(self.root, text="Student Login", font=("times", 30, "italic bold"), cursor="hand2",
                         borderwidth=8, bg="yellowgreen",activebackground="blue",command=self.new_acc)
        student.place(x=1005, y=115)

        stud()

    def login(self):
        self.root.destroy()
        import login

    def new_acc(self):
        self.root.destroy()
        import regester


root=Tk()
obj=welcome(root)


con=pymysql.connect(host="localhost",user="root",password="06081998",port=3307)
mycursor=con.cursor()

try:
    strr = "create database Management"
    mycursor.execute(strr)

    strr="use management"
    mycursor.execute(strr)

    #-------------------------------------------------------------------------------------------

    strr = "create table faculty(ID varchar(10) , Name varchar(25) , password varchar(20))"
    mycursor.execute(strr)

    strr = "alter table faculty modify column ID varchar(10) not Null"
    mycursor.execute(strr)

    strr = "alter table faculty modify column ID varchar(10) primary key"
    mycursor.execute(strr)

    strr = "use management"
    mycursor.execute(strr)

    strr = """insert into faculty(ID , Name , password)values("F070","Sudeep Pandey",12345)"""
    mycursor.execute(strr)
    con.commit()

    strr = """insert into faculty(ID , Name , password)values("F060","Rahul Singh",12345)"""
    mycursor.execute(strr)
    con.commit()

    strr = """insert into faculty(ID , Name , password)values("F063","Devesh Pandey",12345)"""
    mycursor.execute(strr)
    con.commit()

    strr = """insert into faculty(ID , Name , password)values("F034","Anand Tiwari",12345)"""
    mycursor.execute(strr)
    con.commit()

    strr = """insert into faculty(ID , Name , password)values("F071","Rjendra",12345)"""
    mycursor.execute(strr)
    con.commit()

    #--------------------------------------------------------------------------------------------------


except:
     messagebox.showinfo("Message","Your Database is already Created",parent=root)
# except Exception as es:
#     messagebox.showerror("Error"f"Error Due to: {str(es)}",parent=root)



root.mainloop()
