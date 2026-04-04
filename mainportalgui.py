import tkinter
from signupgui import signup
from logingui import login
from tkinter import ttk

window=tkinter.Tk()
window.title("AgniVeer Recruitment System")
frame=tkinter.Frame(window)
frame.pack()
f=tkinter.LabelFrame(frame)
f.grid(row=0,column=0,padx=50,pady=50)

welcome_label=tkinter.Label(f,text="\t\tWelcome to AgniVeer Recruitment Portal\t\t",font=("Comic Sans MS", 20,"bold"))
welcome_label.grid(row=0,column=0)

spc=tkinter.Label(f,text="")

msg1_label=tkinter.Label(f,text="India's youth is set to play a crucial role in realising the dream of building an AatmaNirbhar, Sashakt Bharat.",font=("Comic Sans MS", 11,"bold"))
msg1_label=tkinter.Label(f,text="And Agnipath scheme will take them a step closer. It is a unique opportunity to fulfil their dream of joining the Armed Forces & serving the Nation.",font=("Comic Sans MS", 11,"bold"))

for widgit in f.winfo_children():
    widgit.grid_configure(padx=10,pady=5)

b1=tkinter.Button(frame,text="SIGN UP",command=signup,font=("Cambria",20,"bold"))
b1.grid(row=1,column=0,padx=50,pady=50)

b2=tkinter.Button(frame,text="LOGIN",command=login,font=("Cambria",20,"bold"))
b2.grid(row=2,column=0,padx=50,pady=50)

b3=tkinter.Button(frame,text="EXIT",command=exit,font=("Cambria",20,"bold"))
b3.grid(row=3,column=0,padx=50,pady=50)

window.mainloop()
