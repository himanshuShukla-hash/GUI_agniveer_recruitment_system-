import tkinter
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

mydb= mysql.connector.connect(host='localhost',user='Vedansh Gandharva',password='root',database="AgniVeer")
c=mydb.cursor()
sc="war"

def recsignup():
    window=tkinter.Tk()
    window.title("AgniVeer Recruit SignUp System")
    frame=tkinter.Frame(window)
    frame.pack()
    
    def pwdverif():
        p=pwd_entry.get()
        rp=repwd_entry.get()
        n=name_entry.get()
        m=mail_entry.get()
        if p==rp:
            q1="INSERT INTO recruitlogincred (name,mail,pwd) VALUES (%s,%s,%s)"
            v1=(n,m,p)
            c.execute(q1,v1)
            mydb.commit()
            tkinter.messagebox.showwarning(title="Success",message="Your account was created Successfully")
        else:
            tkinter.messagebox.showwarning(title="Error",message="Your passwords don't match!")
    
    user_info_frame=tkinter.LabelFrame(frame,text="User Information")
    user_info_frame.grid(row=0,column=0,padx=50,pady=50)
    
    name_label=tkinter.Label(user_info_frame,text="User Name")
    name_label.grid(row=0,column=0)
    name_entry=tkinter.Entry(user_info_frame)
    name_entry.grid(row=1,column=0)
    
    mail_label=tkinter.Label(user_info_frame,text="Mail ID")
    mail_label.grid(row=2,column=0)
    mail_entry=tkinter.Entry(user_info_frame)
    mail_entry.grid(row=3,column=0)
    
    pwd_info_frame=tkinter.LabelFrame(frame,text="Password Information")
    pwd_info_frame.grid(row=0,column=2,padx=50,pady=50)
    
    pwd_label=tkinter.Label(pwd_info_frame,text="Password")
    pwd_label.grid(row=0,column=2)
    pwd_entry=tkinter.Entry(pwd_info_frame)
    pwd_entry.grid(row=1,column=2)
    
    repwd_label=tkinter.Label(pwd_info_frame,text="Re-enter Password")
    repwd_label.grid(row=2,column=2)
    repwd_entry=tkinter.Entry(pwd_info_frame)
    repwd_entry.grid(row=3,column=2)
    
    for widgit in pwd_info_frame.winfo_children():
        widgit.grid_configure(padx=10,pady=5)
    
    b=tkinter.Button(frame,text="Create Account",command=pwdverif)
    b.grid(row=5,column=1,padx=50,pady=50)
    
    window.mainloop()

def offsignup():
    window=tkinter.Tk()
    window.title("AgniVeer Officer SignUp System")
    frame=tkinter.Frame(window)
    frame.pack()
    
    def dataverif():
        p=pwd_entry.get()
        rp=repwd_entry.get()
        n=name_entry.get()
        m=mail_entry.get()
        sci=sccode_entry.get()
        if sci==sc:
            q1="INSERT INTO officerlogincred (name,mail,pwd) VALUES (%s,%s,%s)"
            v1=(n,m,p)
            c.execute(q1,v1)
            mydb.commit()
            tkinter.messagebox.showwarning(title="Success",message="Your account was created Successfully")
        else:
            tkinter.messagebox.showwarning(title="Error",message="Enter valid Officer's Secret Code!")
    
    user_info_frame=tkinter.LabelFrame(frame,text="User Information")
    user_info_frame.grid(row=0,column=0,padx=50,pady=50)
    
    name_label=tkinter.Label(user_info_frame,text="User Name")
    name_label.grid(row=0,column=0)
    name_entry=tkinter.Entry(user_info_frame)
    name_entry.grid(row=1,column=0)
    
    mail_label=tkinter.Label(user_info_frame,text="Mail ID")
    mail_label.grid(row=2,column=0)
    mail_entry=tkinter.Entry(user_info_frame)
    mail_entry.grid(row=3,column=0)
    
    sccode_label=tkinter.Label(user_info_frame,text="Officer's Secret Code")
    sccode_label.grid(row=4,column=0)
    sccode_entry=tkinter.Entry(user_info_frame)
    sccode_entry.grid(row=5,column=0)
    
    pwd_info_frame=tkinter.LabelFrame(frame,text="Password Information")
    pwd_info_frame.grid(row=0,column=2,padx=50,pady=50)
    
    pwd_label=tkinter.Label(pwd_info_frame,text="Password")
    pwd_label.grid(row=0,column=2)
    pwd_entry=tkinter.Entry(pwd_info_frame)
    pwd_entry.grid(row=1,column=2)
    
    repwd_label=tkinter.Label(pwd_info_frame,text="Re-enter Password")
    repwd_label.grid(row=2,column=2)
    repwd_entry=tkinter.Entry(pwd_info_frame)
    repwd_entry.grid(row=3,column=2)
    
    for widgit in pwd_info_frame.winfo_children():
        widgit.grid_configure(padx=10,pady=5)
    
    b=tkinter.Button(frame,text="Create Account",command=dataverif)
    b.grid(row=5,column=1,padx=50,pady=50)
    
    window.mainloop()

def signup():
    window=tkinter.Tk()
    window.title("AgniVeer SignUp System")
    frame=tkinter.Frame(window)
    frame.pack()
    
    f=tkinter.LabelFrame(frame)
    f.grid(row=0,column=0,padx=50,pady=50)
    
    for widgit in f.winfo_children():
        widgit.grid_configure(padx=10,pady=5)
    
    b1=tkinter.Button(frame,text="RECRUIT's SIGNUP",command=recsignup,font=("Cambria",20,"bold"))
    b1.grid(row=1,column=0,padx=50,pady=50)
    
    b2=tkinter.Button(frame,text="OFFICER's SIGNUP",command=offsignup,font=("Cambria",20,"bold"))
    b2.grid(row=2,column=0,padx=50,pady=50)
