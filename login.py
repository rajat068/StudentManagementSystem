from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql



class Login_system:


    
    def __init__(self,root):
        self.root=root
        self.root.title("Allen Management")
        self.root.geometry("1350x700+0+15")
        #-------------------All Images-------------
        self.bg_icon=ImageTk.PhotoImage(file="862737.png")
        self.user_icon=PhotoImage(file="21104.png")
        self.logo_icon=PhotoImage(file="unnamed.png")
        self.pass_icon=PhotoImage(file="lock.png")

        
        bg=Label(self.root,image=self.bg_icon).pack()
        
        title=Label(self.root,text="Allen Management System",font=("times",35,"italic bold"),bg="navy",fore="cyan",bd=10,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)

        Login_Frame=Frame(self.root,bg="white")
        Login_Frame.place(x=400,y=150)

        lo=Label(Login_Frame,text="Login Here",font=("times",20,"italic bold"),bg="white",fg="#08A3D2")
        lo.place(x=20,y=30)

        logo=Label(Login_Frame,image=self.logo_icon,bd=0).grid(row=0,columnspan=2,pady=20)
        user=Label(Login_Frame,text="User Name",image=self.user_icon,compound=LEFT,bg="white",font=("times",20,"italic bold")).grid(row=1,column=0,padx=20,pady=10)
        Password=Label(Login_Frame,text="Password",image=self.pass_icon,compound=LEFT,bg="white",font=("times",20,"italic bold")).grid(row=2,column=0,padx=20,pady=10)
        
        #------------------variables----------------
        # self.uname=StringVar()
        # self.pass_=StringVar()
        
        self.userentry=Entry(Login_Frame,bd=5,relief=GROOVE,font=("times",15,"italic bold"))
        self.userentry.grid(row=1,column=1,padx=20)
        self.passentry=Entry(Login_Frame,bd=5,relief=GROOVE,font=("times",15,"italic bold"),show="*")
        self.passentry.grid(row=2,column=1,padx=20)

        loginbutt=Button(Login_Frame,text="Login",width=15,font=("times",15,"italic bold"),relief=RIDGE,bd=5,bg="cyan4",
                         activebackground="green",activeforeground="blue",command=self.login).grid(row=3,column=1,pady=10)

        newacc=Button(Login_Frame,text="Requierd New Account ?",width=20,font=("times",12,"italic"),bg="white",borderwidth=0,
                      fg="#b00857",command=self.new_acc)
        newacc.place(x=35,y=335)
#_________________________________________________________________________________#
    def dbms(self):
        self.root.destroy()
        import dbms

    def daa(self):
        self.root.destroy()
        import DAA

    def compiler(self):
        self.root.destroy()
        import compiler

    def webd(self):
        self.root.destroy()
        import webd

    def ml(self):
        self.root.destroy()
        import machine

    def student(self):
        self.root.destroy()
        import student

    def new_acc(self):
        self.root.destroy()
        import regester

#___________________________________________________________________________________#
  
    def login(self):

        Host="localhost"
        User="root"
        Password="06081998"


        if self.userentry.get()=="" or self.passentry.get()=="":
            messagebox.showerror("Error","All Feilds are Required!!",parent=self.root)
        else:
            try:
                con = pymysql.connect(host=Host, user=User, password=Password, port=3307)
                mycursor = con.cursor()

                strr = "use Management"
                mycursor.execute(strr)
                try:

                 if self.userentry.get() == 'F070' and self.passentry.get()== '12345':
                    messagebox.showinfo("Success", "Login Successfully", parent=self.root)
                    self.dbms()

                 elif self.userentry.get() == 'F060' and self.passentry.get()== '12345':
                    messagebox.showinfo("Success", "Login Successfully", parent=self.root)
                    self.daa()

                 elif self.userentry.get() == 'F063' and self.passentry.get()== '12345':
                    messagebox.showinfo("Success", "Login Successfully", parent=self.root)
                    self.compiler()

                 elif self.userentry.get() == 'F034' and self.passentry.get()== '12345':
                    messagebox.showinfo("Success", "Login Successfully", parent=self.root)
                    self.webd()

                 elif self.userentry.get() == 'F071' and self.passentry.get()== '12345':
                    messagebox.showinfo("Success", "Login Successfully", parent=self.root)
                    self.ml()



                 else:
                     strr = "select * from student where RollNo=%s and Password=%s"
                     mycursor.execute(strr, (self.userentry.get(), self.passentry.get()))
                     data1 = mycursor.fetchone()

                     if data1 == None:
                         messagebox.showerror("Error", "Invalid username and password", parent=self.root)
                     else:
                         messagebox.showinfo("Success", "Login Successfully", parent=self.root)

                         self.student()

                except:
                    messagebox.showerror("Error", "Invalid username and password", parent=self.root)

                    
            except Exception as es:
                 messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self.root)

root = Tk()
obj = Login_system(root)

root.mainloop()