from tkinter import *
import tkinter.ttk as ttk
import random
from tkinter import messagebox
import pymysql

color = ["blue", "red"]
#---------------------------------show Data------------------------------------------#
con=pymysql.connect(host="localhost",user="root",password="06081998",port=3307)
mycursor=con.cursor()
strr="use Management"
mycursor.execute(strr)

def Show():
    s="Web_D"
    #_______________________only first one is working __________________________________   
    strr="select * from CT where Subject=%s"
    mycursor.execute(strr,s)
    Data=mycursor.fetchall()
    strr = "select * from CT order by RollNo"
    mycursor.execute(strr)

    StudentTable.delete(*StudentTable.get_children())
    for i in Data:
        vv=[i[0],i[1],i[2],i[3],i[4]]
        StudentTable.insert("",END,values=vv) 
    




#     ################-----------------------------Show student result------------------------------##########


# ---------------------------------------------------------------------------------
def showresult():
    def Submitsearch():
        global mycursor
        roll = rollval.get()
        name = nameval.get()
        var=cmb_quest.get()
        var1=varval.get()
        s="Web_D"
        if var1=="CT":
            if (roll != ""):
                strr = "select * from CT where RollNo=%s and subject=%s"
                mycursor.execute(strr, (roll,s))
                Data = mycursor.fetchall()
                StudentTable.delete(*StudentTable.get_children())
                for i in Data:
                    vv = [i[0], i[1], i[2], i[3],i[4],i[5]]
                    StudentTable.insert("", END, values=vv)
            elif (name != ""):
                strr = "select * from CT where Name=%s and subject=%s"
                mycursor.execute(strr, (name,s))
                Data = mycursor.fetchall()
                StudentTable.delete(*StudentTable.get_children())
                for i in Data:
                    vv = [i[0], i[1], i[2], i[3],i[4],i[5]]
                    StudentTable.insert("", END, values=vv)
            elif var=="Hostel":
                strr = " select ERPNo,name,Exam,ObtainMarks,TotalMarks,user from student,CT where User=%s and Subject=%s and Student.RollNo=CT.RollNo"
                mycursor.execute(strr, (var,s))
                Data = mycursor.fetchall()
                StudentTable.delete(*StudentTable.get_children())
                for i in Data:
                    vv = [i[0], i[1], i[2], i[3],i[4],i[5]]
                    StudentTable.insert("", END, values=vv)
            elif var=="Bus":
                strr = " select ERPNo,name,Exam,ObtainMarks,TotalMarks,user from student,CT where User=%s and Subject=%s and Student.RollNo=CT.RollNo"
                mycursor.execute(strr, (var,s))
                Data = mycursor.fetchall()
                StudentTable.delete(*StudentTable.get_children())
                for i in Data:
                    vv = [i[0], i[1], i[2], i[3],i[4],i[5]]
                    StudentTable.insert("", END, values=vv)
        else:
            if (roll != ""):
                strr = "select * from PUT where RollNo=%s and subject=%s"
                mycursor.execute(strr, (roll,s))
                Data = mycursor.fetchall()
                StudentTable.delete(*StudentTable.get_children())
                for i in Data:
                    vv = [i[0], i[1], i[2], i[3],i[4],i[5]]
                    StudentTable.insert("", END, values=vv)
            elif (name != ""):
                strr = "select * from PUT where Name=%s and subject=%s"
                mycursor.execute(strr, (name,s))
                Data = mycursor.fetchall()
                StudentTable.delete(*StudentTable.get_children())
                for i in Data:
                    vv = [i[0], i[1], i[2], i[3],i[4],i[5]]
                    StudentTable.insert("", END, values=vv)
            elif var=="Hostel":
                strr = " select ERPNo,name,Exam,ObtainMarks,TotalMarks,user from student,PUT where User=%s and Subject=%s and Student.RollNo=PUT.RollNo"
                mycursor.execute(strr, (var,s))
                Data = mycursor.fetchall()
                StudentTable.delete(*StudentTable.get_children())
                for i in Data:
                    vv = [i[0], i[1], i[2], i[3],i[4],i[5]]
                    StudentTable.insert("", END, values=vv)
            elif var=="Bus":
                strr = " select ERPNo,name,Exam,ObtainMarks,TotalMarks,user from student,PUT where User=%s and Subject=%s and Student.RollNo=PUT.RollNo"
                mycursor.execute(strr, (var,s))
                Data = mycursor.fetchall()
                StudentTable.delete(*StudentTable.get_children())
                for i in Data:
                    vv = [i[0], i[1], i[2], i[3],i[4],i[5]]
                    StudentTable.insert("", END, values=vv)
                    




    searchroot = Toplevel(master=buts)
    searchroot.grab_set()
    searchroot.geometry("580x400+350+230")
    searchroot.config(bg="cornflowerblue")
    # ---------------------------------------------------------------search student result
    insert = Label(searchroot, text="--------------Search Student Result-------------", width=20,
                   font=("times", 20, "italic bold"), foreground="white", bg="cornflowerblue")
    insert.place(x=115, y=3)
    roll = Label(searchroot, text="Student Roll No:-", font=("times", 20, "italic bold"), bg="lavender", relief=GROOVE,
                 borderwidth=5, width=15)
    roll.place(x=10, y=60)

    opt = Label(searchroot, text="OR", font=("times", 22, "italic bold"), bg="cornflowerblue", foreground="white")
    opt.place(x=265, y=135)

    name = Label(searchroot, text="Student Name:-", font=("times", 20, "italic bold"), bg="lavender", relief=GROOVE,
                 borderwidth=5, width=15)
    name.place(x=10, y=200)

    # --------------------------------------------------------------------Student-Entry
    nameval = StringVar()
    rollval = StringVar()
    varval=StringVar()
    varval.set("Radio")

    rollentry = Entry(searchroot, font=("times", 20, "italic bold"), relief=GROOVE, bd=5, textvariable=rollval)
    rollentry.place(x=280, y=60)
    nameentry = Entry(searchroot, font=("times", 20, "italic bold"), relief=GROOVE, bd=5, textvariable=nameval)
    nameentry.place(x=280, y=200)

    cmb_quest=ttk.Combobox(searchroot,font=("times",13,"italic"),state="readonly",justify=CENTER)
    cmb_quest["values"]=("Select","Hostel","Bus")
    cmb_quest.place(x=150,y=255,width=250)
    cmb_quest.current(0)

    r=Radiobutton(searchroot,text="CT",padx=14,value="CT",font=("times", 15, "italic bold"),bg="cornflowerblue",variable=varval)
    r.place(x=100,y=135)

    r=Radiobutton(searchroot,text="PUT",padx=14,value="PUT",font=("times", 15, "italic bold"),bg="cornflowerblue",variable=varval)
    r.place(x=400,y=135)

    addSubject = Button(searchroot, text="search Result", font=("times", 15, "italic bold"), width=20,
                        activebackground="green", activeforeground="white", bd=5, command=Submitsearch)
    addSubject.place(x=165, y=330)

    searchroot.mainloop()

    ##------------------------------------Add student information----------------------------#

    # ---------------------------------------add result--------------------------------#


def addresut():
    def Subresult():
        roll = rollval.get()
        name = nameval.get()
        Web_D = Web_Dval.get()
        s="Web_D"
        if cmb_quest.get()=="CT:-1" or cmb_quest.get()=="CT:-2":
            T = 30
            try:

                strr="use Management"
                mycursor.execute(strr)
                strr="create table CT(RollNo int,Name varchar(20),Exam varchar(10),Subject varchar(20),ObtainMarks int,TotalMarks int)"
                mycursor.execute(strr)
                strr = "alter table CT modify column RollNo int not null"
                mycursor.execute(strr)
                strr = " ALTER TABLE CT ADD FOREIGN KEY (RollNo) REFERENCES student(RollNo)"
                mycursor.execute(strr)
                strr = "insert into CT(RollNo,Name,Exam,Subject,ObtainMarks,TotalMarks)values(%s,%s,%s,%s,%s,%s)"
                mycursor.execute(strr, (roll,name,cmb_quest.get(),s,Web_D, T))
                con.commit()
                messagebox.showinfo("Notification","Added Sucessfully...." ,parent=addroot)

            except:
                strr="use Management"
                mycursor.execute(strr)
                strr="select * from CT where RollNo=%s and Subject=%s and Exam=%s"
                mycursor.execute(strr,(roll,s,cmb_quest.get()))
                Data=mycursor.fetchone()
                if Data!=None:
                    messagebox.showerror("Notification", "Id Already Exist try another id.....", parent=addroot)
                    return
                else:
                    strr = "insert into CT(RollNo,Name,Exam,Subject,ObtainMarks,TotalMarks)values(%s,%s,%s,%s,%s,%s)"
                    mycursor.execute(strr, (roll,name,cmb_quest.get(),s,Web_D, T))
                    con.commit()
                    messagebox.showinfo("Notification","Added Sucessfully...." ,parent=addroot)


        else:
            T=50
            try:
                strr="use Management"
                mycursor.execute(strr)
                strr="create table PUT(RollNo int,Name varchar(20),Exam varchar(10),Subject varchar(20),ObtainMarks int,TotalMarks int)"
                mycursor.execute(strr)
                strr = "alter table PUT modify column RollNo int not null"
                mycursor.execute(strr)
                strr = "ALTER TABLE PUT ADD FOREIGN KEY (RollNo) REFERENCES student(RollNo)"
                mycursor.execute(strr)
                # strr = "alter table PUT add foreign key(RollNO) References CT(RollNO)"
                # mycursor.execute(strr)
                strr = "insert into PUT(RollNo,Name,Exam,Subject,ObtainMarks,TotalMarks)values(%s,%s,%s,%s,%s,%s)"
                mycursor.execute(strr, (roll,name,cmb_quest.get(),s,Web_D, T))
                con.commit()
                messagebox.showinfo("Notification","Added Sucessfully...." ,parent=addroot)
            except:
                strr="use Management"
                mycursor.execute(strr)
                strr="select * from PUT where RollNo=%s and Subject=%s"
                mycursor.execute(strr,(roll,s))
                Data=mycursor.fetchone()
                if Data!=None:
                    messagebox.showerror("Notification", "Id Already Exist try another id.....", parent=addroot)
                    return
                else:
                    strr = "insert into PUT(RollNo,Name,Exam,Subject,ObtainMarks,TotalMarks)values(%s,%s,%s,%s,%s,%s)"
                    mycursor.execute(strr, (roll,name,cmb_quest.get(),s,Web_D, T))
                    con.commit()
                    messagebox.showinfo("Notification","Added Sucessfully...." ,parent=addroot)

            




    addroot = Toplevel(master=buts)
    addroot.grab_set()
    addroot.geometry("590x450+400+130")
    addroot.config(bg="cornflowerblue")

    insert = Label(addroot, text="-----------Welcome----------", width=25, font=("times", 20, "italic bold"),
                   foreground="white", bg="cornflowerblue")
    insert.place(x=115, y=5)

    roll = Label(addroot, text="Student Roll No:-", font=("times", 20, "italic bold"), bg="lavender", relief=GROOVE,
                 borderwidth=5, width=15)
    roll.place(x=10, y=50)

    name = Label(addroot, text="Student Name:-", font=("times", 20, "italic bold"), bg="lavender", relief=GROOVE,
                 borderwidth=5, width=15)
    name.place(x=10, y=120)

    info = Label(addroot, text="-------↓↓↓↓Enter Subject No.↓↓↓↓-------", width=30, font=("times", 20, "italic bold"),
                 foreground="white", bg="cornflowerblue")
    info.place(x=50, y=180)

    Web_D = Label(addroot, text="Web_D:-", font=("times", 20, "italic bold"), bg="lavender", relief=GROOVE, borderwidth=5,
                 width=15)
    Web_D.place(x=10, y=250)

    # ______________________________________enter subject no._________________________________#

    nameval = StringVar()
    rollval = StringVar()
    Web_Dval = IntVar()
    



    rollentry = Entry(addroot, font=("times", 20, "italic bold"), relief=GROOVE, bd=5, textvariable=rollval)
    rollentry.place(x=280, y=50)
    nameentry = Entry(addroot, font=("times", 20, "italic bold"), relief=GROOVE, bd=5, textvariable=nameval)
    nameentry.place(x=280, y=120)

    Web_Dentry = Entry(addroot, font=("times", 20, "italic bold"), relief=GROOVE, bd=5, textvariable=Web_Dval)
    Web_Dentry.place(x=280, y=250)

    cmb_quest=ttk.Combobox(addroot,font=("times",13,"italic"),state="readonly",justify=CENTER)
    cmb_quest["values"]=("Select","CT:-1","CT:-2","PUT")
    cmb_quest.place(x=150,y=330,width=250)
    cmb_quest.current(0)


    submitresult = Button(addroot, text="Submit Result", font=("times", 15, "italic bold"), width=20,
                          activebackground="green", activeforeground="white", bd=5, command=Subresult)
    submitresult.place(x=160, y=400)

    addroot.mainloop()


# ----------------------------------------------------------------------------------------
def introcolor():
    fg = random.choice(color)
    SliderLable.config(fg=fg)
    SliderLable.after(20, introcolor)


# -----------------------------------------------------------------------------------
def Intro():
    global count, text
    if (count >= len(ss)):
        count = 0
        text = " "
        SliderLable.config(text=text)
    else:
        text = text + ss[count]
        SliderLable.config(text=text)
        count = count + 1
    SliderLable.after(200, Intro)


# -------------------------------------------------------main window
root = Tk()
from tkinter.ttk import Treeview

# imagehome=PhotoImage(file="123.png")
# label=ttk.Label(image=imagehome)
# label.place(x=5,y=0)
root.geometry("1280x720+40+10")
root.config(bg="light blue")
root.title("Student Management System")
root.resizable(False, False)
# -------------------------------------------------------------------buttons Frame
buts = Frame(root, bg="light grey", relief=RIDGE, borderwidth=5)
buts.place(y=550, width=1280, height=170)
# -------------------------------------------------------------------Data Base Connection Button

# -------------------------------------------------------------------Student Add Button
insert = Button(buts, text="Add Student Result", width=16, font=("times", 20, "italic bold"), relief=GROOVE, bd=12,
                bg="skyblue3", activebackground="blue", activeforeground="white", command=addresut)
insert.place(x=5, y=55)

search = Button(buts, text="Search Student Result", width=16, font=("times", 20, "italic bold"), relief=GROOVE, bd=12,
              bg="skyblue3", activebackground="blue", activeforeground="white", command=showresult)
search.place(x=470, y=55)

show = Button(buts, text="Show Student Result", width=16, font=("times", 20, "italic bold"), relief=GROOVE, bd=12,
              bg="skyblue3", activebackground="blue", activeforeground="white",command=Show)
show.place(x=900, y=55)

# --------------------------------------------------------------------Data Show Frame
data = Frame(root, bg="White", relief=RIDGE, borderwidth=5)
data.place(y=70, width=1280, height=480)

style = ttk.Style()
style.configure("Treeview.Heading", font=("times", 20, "italic bold"), foreground="red")
style.configure("Treeview", font=("times", 15, " italic bold"), foreground="white", background="cornflowerblue")
Scroll_x = Scrollbar(data, orient=HORIZONTAL)
Scroll_y = Scrollbar(data, orient=VERTICAL)
StudentTable = ttk.Treeview(data, columns=(
"RollNo", "Name", "Exam", "Web_D",  "TotalMarks"),
                            yscrollcommand=Scroll_y.set, xscrollcommand=Scroll_x.set)
Scroll_x.pack(side=BOTTOM, fill=X)
Scroll_y.pack(side=RIGHT, fill=Y)
Scroll_x.config(command=StudentTable.xview)
Scroll_y.config(command=StudentTable.yview)

StudentTable.heading("RollNo", text="RollNo")
StudentTable.heading("Name", text="Name")
StudentTable.heading("Exam", text="Exam")
StudentTable.heading("Web_D", text="Web_D")
StudentTable.heading("TotalMarks", text="TotalMarks")
StudentTable["show"] = "headings"

StudentTable.column("RollNo",width=180)
StudentTable.column("Name",width=210)
StudentTable.column("Exam",width=100)
StudentTable.column("Web_D",width=90)
StudentTable.column("TotalMarks",width=210)
StudentTable.pack(fill=BOTH, expand=1)
# --------------------------------------------------------------------SliderWelcome
ss = "WEB DESIGNING"
count = 0
text = " "
SliderLable = Label(root, text=ss, font=("times", 30, "italic bold"), relief=RIDGE, borderwidth=0, width=30,
                    bg="light blue")
SliderLable.place(x=220)
Intro()
introcolor()
root.mainloop()
