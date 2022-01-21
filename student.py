from tkinter import *
from PIL import Image , ImageTk
import random
import pymysql
from tkinter import messagebox
import webbrowser as wb
x=1

color = ["blue", "red"]


class welcome:



    def __init__(self,root):




        self.root = root
        self.root.config(bg="paleturquoise")
        self.root.title("Student Window")
        self.root.geometry("1350x600+70+50")
        # -----------------bg image--------------------------

        image1 = ImageTk.PhotoImage(file="all1.jpg")
        image2 = ImageTk.PhotoImage(file="all2.jpg")
        image3 = ImageTk.PhotoImage(file="all3.jpg")
        image4 = ImageTk.PhotoImage(file="all4.jpg")


        self.frame_slider = Frame(self.root)
        self.frame_slider.place(x=0, y=0, relwidth=1, height=400)

        l = Label(self.frame_slider, font="bold")
        l.pack()



        def move():

            global x
            if x == 5:
                x = 1
            if x == 1:
                l.config(image=image1)
            elif x == 2:
                l.config(image=image2)
            elif x == 3:
                l.config(image=image3)
            elif x == 4:
                l.config(image=image4)
            x += 1
            root.after(2000, move)
        move()

        result = Button(self.root, text="Show Result", font=("times", 30, "italic bold"), cursor="hand2", borderwidth=8,
                        bg="cornflowerblue", activebackground="blue")
        result.place(x=50, y=445)

        TT = Button(self.root, text="Time Table", font=("times", 30, "italic bold"), cursor="hand2", borderwidth=8,
                    bg="cornflowerblue", activebackground="blue",command=self.showresult)
        TT.place(x=390, y=445)

        notice = Button(self.root, text="Notice board", font=("times", 30, "italic bold"), cursor="hand2",
                        borderwidth=8,
                        bg="cornflowerblue", activebackground="blue",command=self.notice)
        notice.place(x=730, y=445)

        pfm = Button(self.root, text="Performance", font=("times", 30, "italic bold"), cursor="hand2", borderwidth=8,
                     bg="cornflowerblue", activebackground="blue",command= self.login)
        pfm.place(x=1070, y=445)

    def showresult(self):
        # wb.open_new('csett.pdf')
        searchroot = Toplevel(master=self.root)
        searchroot.grab_set()
        searchroot.geometry("1350x720+50+10")
        searchroot.config(bg="cornflowerblue")

        self.bg = ImageTk.PhotoImage(file="time.jpg")
        bg = Label(searchroot, image=self.bg)
        bg.place(x=0, y=0, relwidth=1, relheight=1)


        searchroot.mainloop()

    def notice(self):
        #wb.open_new('csett.pdf')
        noticeroot = Toplevel(master=self.root)
        noticeroot.grab_set()
        noticeroot.geometry("1350x720+50+10")
        noticeroot.config(bg="light green")

        def teach():
            fg = random.choice(color)
            noti.config(fg=fg)
            noti.after(20, teach)

        noti = Label(noticeroot, text='↓↓↓↓Notice Board↓↓↓↓', font=("times", 30, "italic bold"),
                    bg="light green", foreground="maroon")
        noti.place(x=500, y=10)
        teach()


        noticeroot.mainloop()

    def perform(self):
        performroot = Toplevel(master=self.root)
        performroot.grab_set()
        performroot.geometry("400x220+600+250")
        performroot.config(bg="light grey")
        varval = StringVar()
        varval.set("Radio")

        cor = Label(performroot,text='↓↓↓↓Check Your Performance↓↓↓↓',font=("times",20,"italic bold"), bg="light grey",foreground="maroon")
        cor.place(x=0, y=10)

        ct1 = Radiobutton(performroot, text="CT:-1",value='CT1', padx=14, font=("times", 25, "italic bold"),foreground="blue",
                        bg="light grey",variable=varval)
        ct1.place(x=10, y=75)

        put = Radiobutton(performroot, text="PUT",value='PUT', padx=14, font=("times", 25, "italic bold"), foreground="blue",
                          bg="light grey",variable=varval)
        put.place(x=138, y=75)

        ct2 = Radiobutton(performroot, text="CT:-2",value='CT2', padx=14, font=("times", 25, "italic bold"), foreground="blue",
                          bg="light grey",variable=varval)
        ct2.place(x=252, y=75)

        pfmbtn = Button(performroot, text="CHECK", font=("times", 20, "italic bold"), cursor="hand2", borderwidth=8,
                     bg="cornflowerblue", activebackground="blue")
        pfmbtn.place(x=140, y=150)

        performroot.mainloop()

    def login(self):
            try:
                con = pymysql.connect(host="localhost", user="root", password="06081998", port=3307)
                mycursor = con.cursor()

                strr = "use Management"
                mycursor.execute(strr)
                strr = "select ObtainMarks from ct where RollNo=""1850510010"""
                mycursor.execute(strr)
                data1=mycursor.fetchall()
                print(data1)


            except Exception as es:
                messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self.root)






root=Tk()
obj=welcome(root)
root.mainloop()

