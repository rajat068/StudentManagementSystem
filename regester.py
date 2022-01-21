from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pymysql

class Register:
    
       
    
    def __init__(self,root):
        self.root=root
        self.root.config(bg="white")
        self.root.title("Registration Window")
        self.root.geometry("1350x720+2+10")
        #-----------------bg image--------------------------
        self.bg=ImageTk.PhotoImage(file="862737.png")
        bg=Label(self.root,image=self.bg)
        bg.place(x=250,y=0,relwidth=1,relheight=1)       
        #--------------------corner bg---------------------------------
        self.cor=ImageTk.PhotoImage(file="images (1).jpg")
        cor=Label(self.root,image=self.cor,bg="gold2")
        cor.place(x=30,y=10,width=200,height=700)
        #----------------Register frame---------------------------------
        reg=Frame(self.root,bg="white")
        reg.place(x=480,y=100,width=700,height=520)
        #---------------- Row 0 Register frame Title---------------------------------
        tit=Label(reg,text="REGISTER HERE",font=("times",20,"italic bold"),bg="white",fg="green")
        tit.place(x=50,y=30)
        #-------------------------- Row 1 First Name + Entry------------------------
        f_name=Label(reg,text="First Name",font=("times",15,"italic bold"),bg="white",fg="grey")
        f_name.place(x=50,y=100)
        self.txt_fname=Entry(reg,font=("times",15,"italic"),bg="lightgrey")
        self.txt_fname.place(x=50,y=130,width=250)
        #----------------------Last Name + Entry------------------------
        l_name=Label(reg,text="Last Name",font=("times",15,"italic bold"),bg="white",fg="grey")
        l_name.place(x=370,y=100)
        self.txt_lname=Entry(reg,font=("times",15,"italic"),bg="lightgrey")
        self.txt_lname.place(x=370,y=130,width=250)

        #-------------------------- Row 2 contact number +Entry------------------------
        contact=Label(reg,text="Contact",font=("times",15,"italic bold"),bg="white",fg="grey")
        contact.place(x=50,y=170)
        self.txt_contact=Entry(reg,font=("times",15,"italic"),bg="lightgrey")
        self.txt_contact.place(x=50,y=200,width=250)
        #----------------------Email + Entry------------------------
        email=Label(reg,text="Email",font=("times",15,"italic bold"),bg="white",fg="grey")
        email.place(x=370,y=170)
        self.txt_email=Entry(reg,font=("times",15,"italic"),bg="lightgrey")
        self.txt_email.place(x=370,y=200,width=250)
        #-------------------------- Row 3 Security Question ------------------------
        ques=Label(reg,text="SEM:",font=("times",15,"italic bold"),bg="white",fg="grey")
        ques.place(x=50,y=240)

        self.cmb_quest=ttk.Combobox(reg,font=("times",13,"italic"),state="readonly",justify=CENTER)
        self.cmb_quest["values"]=("Semester","1st","2nd","3rd","4th","5th","6th","7th","8th")
        self.cmb_quest.place(x=50,y=270,width=250)
        self.cmb_quest.current(0)
#-----------------------------------------------------user Role-----------------------------------
        self.cmb_quest1=ttk.Combobox(reg,font=("times",13,"italic"),state="readonly",justify=CENTER)
        self.cmb_quest1["values"]=("Select","Hostel","Bus","None")
        self.cmb_quest1.place(x=370,y=270,width=250)
        self.cmb_quest1.current(0)
        ans=Label(reg,text="User",font=("times",15,"italic bold"),bg="white",fg="grey")
        ans.place(x=370,y=240)
         #-------------------------- Row 4 password +Entry------------------------
        self.pas=Label(reg,text="Password",font=("times",15,"italic bold"),bg="white",fg="grey")
        self.pas.place(x=50,y=370)
        self.txt_pas=Entry(reg,font=("times",15,"italic"),bg="lightgrey")
        self.txt_pas.place(x=50,y=400,width=250)

        self.roll=Label(reg,text="Roll No",font=("times",15,"italic bold"),bg="white",fg="grey")
        self.roll.place(x=50,y=310)
        self.txt_roll=Entry(reg,font=("times",15,"italic"),bg="lightgrey")
        self.txt_roll.place(x=50,y=340,width=250)

        self.erp=Label(reg,text="ERP No",font=("times",15,"italic bold"),bg="white",fg="grey")
        self.erp.place(x=370,y=310)
        self.txt_erp=Entry(reg,font=("times",15,"italic"),bg="lightgrey")
        self.txt_erp.place(x=370,y=340,width=250)


        #----------------------Email + Entry------------------------
        self.cpas=Label(reg,text="Confirm Password",font=("times",15,"italic bold"),bg="white",fg="grey")
        self.cpas.place(x=370,y=370)
        self.txt_cpas=Entry(reg,font=("times",15,"italic"),bg="lightgrey")
        self.txt_cpas.place(x=370,y=400,width=250)
        #--------------------------------terms check-------------------------
        self.var_chk=IntVar()
        chk=Checkbutton(reg,text="I Agree To The Terms & Condition",variable=self.var_chk,font=("times",12),onvalue=1,offvalue=0,bg="white")
        chk.place(x=50,y=430)
        #---------------------------------Submit ---------------------------------------
        Register=Button(reg,text="Submit",font=("times",20,"italic bold"),cursor="hand2",relief=RIDGE,bg="green",fg="white",
                        activeforeground="green",activebackground="white",command=self.data)
        Register.place(x=50,y=470,width=200,height=35)
        #---------------------------------sign in-------------------------------------------
        Sign=Button(self.root,text="Sign In",font=("times",20,"italic bold"),cursor="hand2",relief=RIDGE,bg="green",fg="white",
                    activeforeground="green",activebackground="white",command=self.login)
        Sign.place(x=30,y=500,width=200,height=35)

    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_pas.delete(0,END)
        self.txt_cpas.delete(0,END)
        self.cmb_quest.current(0)
        self.cmb_quest1.current(0)
        self.txt_erp.delete(0,END)
        self.txt_roll.delete(0,END)

    def login(self):
        self.root.destroy()
        import login

    def data(self):
        #-------------------------Data Connection------------------------------
        Host="localhost"
        User="root"
        Password="06081998"
            
#-----------------------------------------------------All feild Required--------------------
        if self.txt_fname.get()=="" or self.txt_email.get()=="" or self.txt_contact.get()=="" or self.cmb_quest.get()=="Semester" or self.cmb_quest1.get()=="Select" or self.txt_pas.get()=="" or self.txt_cpas.get()=="":
            messagebox.showerror("Error","All fields Are required",parent=self.root)
        elif self.txt_pas.get()!=self.txt_cpas.get():
            messagebox.showerror("Error","Password & confirm password should be same",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree Our Term & Condition",parent=self.root)
        else:
            try:
                con=pymysql.connect(host=Host,user=User,password=Password,port=3307)
                mycursor=con.cursor()
                # strr="create database Management"
                # mycursor.execute(strr)
                strr="use Management"
                mycursor.execute(strr)
                strr="create table student(RollNo int , ERPNo varchar(100),First_Name varchar(20),Last_Name varchar(10),Contact_Number varchar(15),Email varchar(25),Semester varchar(100),User varchar(100), Password varchar(20))"
                mycursor.execute(strr)
                strr = "alter table student modify column RollNo int not null"
                mycursor.execute(strr)
                strr = "alter table student modify column RollNo int primary key"
                mycursor.execute(strr)
            except:
                strr="use Management"
                mycursor.execute(strr)
                #messagebox.showerror("Error"f"Error Due to: {str(es)}",parent=self.root)

                



            try:
                strr="select * from student where Email=%s"
                mycursor.execute(strr,(self.txt_email.get()))
                data=mycursor.fetchone()
                
                strr="select * from student where Contact_Number=%s"
                mycursor.execute(strr,(self.txt_contact.get()))
                data1=mycursor.fetchone()

                if data!=None or data1!=None:
                  messagebox.showerror("Error","User already exist,please try with another email or Contact Number",parent=self.root)
                else:
                  strr="insert into student(RollNo,ERPNo,First_Name,Last_Name,Contact_Number,Email,Semester,User,Password) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                  mycursor.execute(strr,(self.txt_roll.get(),self.txt_erp.get(),self.txt_fname.get(),self.txt_lname.get(),self.txt_contact.get(),self.txt_email.get(),self.cmb_quest.get(),self.cmb_quest1.get(),self.txt_pas.get()))
                  con.commit()
                  con.close()
                  messagebox.showinfo("Success","Register Successfully",parent=self.root)
                  self.clear()
            except Exception as es:
                messagebox.showerror("Error"f"Error Due to: {str(es)}",parent=self.root)

root=Tk()
obj=Register(root)
root.mainloop()