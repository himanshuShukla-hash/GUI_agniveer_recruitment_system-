import tkinter
import mysql.connector

mydb= mysql.connector.connect(host='localhost',user='Vedansh Gandharva',password='130207',database="AgniVeer")
c=mydb.cursor()

def offlogin():
    window=tkinter.Tk()
    window.title("AgniVeer Officer LogIn System")
    frame=tkinter.Frame(window)
    frame.pack()
    
    def dataverif():
        m=mail_entry.get()
        p=pwd_entry.get()
        q1="SELECT * FROM officerlogincred WHERE mail=%s and pwd=%s"
        c.execute(q1,[m,p])
        r=c.fetchall()
        if r:
            reg()
        else:
            tkinter.messagebox.showwarning(title="Error",message="No data found!")
    
    user_info_frame=tkinter.LabelFrame(frame,text="User Information")
    user_info_frame.grid(row=0,column=0,padx=50,pady=50)
    
    mail_label=tkinter.Label(user_info_frame,text="Mail ID")
    mail_label.grid(row=0,column=0)
    mail_entry=tkinter.Entry(user_info_frame)
    mail_entry.grid(row=1,column=0)
    
    pwd_info_frame=tkinter.LabelFrame(frame,text="Password Information")
    pwd_info_frame.grid(row=1,column=0,padx=50,pady=50)
    
    pwd_label=tkinter.Label(pwd_info_frame,text="Password")
    pwd_label.grid(row=2,column=0)
    pwd_entry=tkinter.Entry(pwd_info_frame)
    pwd_entry.grid(row=3,column=0)
    
    for widgit in pwd_info_frame.winfo_children():
        widgit.grid_configure(padx=10,pady=5)
    
    b=tkinter.Button(frame,text="Login",command=dataverif)
    b.grid(row=5,column=0,padx=50,pady=50)
    
    def reg():
        m=mail_entry.get()
        p=pwd_entry.get()
        q1="SELECT name FROM officerlogincred WHERE mail=%s and pwd=%s"
        c.execute(q1,[m,p])
        r=c.fetchall()
        #coz r is a list with tuple as element inside
        s=r[0][0]
        window=tkinter.Tk()
        window.title("Welcome "+s+" to AgniVeer Recruitment System")
        frame=tkinter.Frame(window)
        frame.pack()
        
        log_info_frame=tkinter.LabelFrame(frame)
        log_info_frame.grid(row=0,column=0,padx=50,pady=50)
        
        for widgit in log_info_frame.winfo_children():
            widgit.grid_configure(padx=10,pady=5)
        
        b1=tkinter.Button(frame,text="ADD A RECRUIT",command=addrec)
        b1.grid(row=1,column=0,padx=50,pady=50)
        
        b2=tkinter.Button(frame,text="GENERATE SUMMARY OF ALL DATA",command=summary)
        b2.grid(row=2,column=0,padx=50,pady=50)
        
        b3=tkinter.Button(frame,text="FIND A RECRUIT's PROFILE",command=filterd)
        b3.grid(row=3,column=0,padx=50,pady=50)
        
        b4=tkinter.Button(frame,text="DELETE A RECRUIT's PROFILE",command=delrec)
        b4.grid(row=1,column=1,padx=50,pady=50)
        
        b5=tkinter.Button(frame,text="UPDATE A RECRUIT's PROFILE",command=updrec)
        b5.grid(row=2,column=1,padx=50,pady=50)
        
        b6=tkinter.Button(frame,text="LOG OUT",command=exit)
        b6.grid(row=3,column=1,padx=50,pady=50)
        
        def addrec():
            def save_recruit_data():
                name = name_entry.get()
                mailid = mailid_entry.get()
                age = age_entry.get()
                qualification = qualification_entry.get()
                height = height_entry.get()
                address = address_entry.get()
                weight = weight_entry.get()
                percentage = percentage_entry.get()
                password=password_entry.get()
                
                mydb = mysql.connector.connect(host='localhost',user='Vedansh Gandharva',password='130207',database="AgniVeer")
                cursor = mydb.cursor()
                
                sql1_insert ="INSERT INTO recruitdata (name, age, qualification, height, address, weight, percentage) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                values = (name, age, qualification, height, address, weight, percentage)
                cursor.execute(sql1_insert, values)
                
                sql2_insert ="INSERT INTO recruitlogincred (name, mail, pwd) VALUES (%s, %s, %s)"
                values = (name, mailid, password)
                cursor.execute(sql2_insert, values)
                
                mydb.commit()
                cursor.close()
                mydb.close()
                tkinter.messagebox.showwarning(title="Success",message="Record was added Successfully")
            
            window = tkinter.Tk()
            
            name_label = tkinter.Label(window, text="Name:")
            name_label.pack()
            name_entry = tkinter.Entry(window)
            name_entry.pack()
            
            mailid_label = tkinter.Label(window, text="Mail Id :")
            mailid_label.pack()
            mailid_entry=tkinter.Entry(window)
            mailid_entry.pack()
            
            age_label = tkinter.Label(window, text="Age:")
            age_label.pack()
            age_entry = tkinter.Spinbox(window, from_='18', to='20')
            age_entry.pack()
            
            qualification_label = tkinter.Label(window, text="Qualification:")
            qualification_label.pack()
            qualification_entry = tkinter.Entry(window)
            qualification_entry.pack()
            
            height_label = tkinter.Label(window, text="Height (in cm):")
            height_label.pack()
            height_entry = tkinter.Entry(window)
            height_entry.pack()
            
            address_label = tkinter.Label(window, text="Address:")
            address_label.pack()
            address_entry = tkinter.Entry(window)
            address_entry.pack()
            
            weight_label = tkinter.Label(window, text="Weight (in kg):")
            weight_label.pack()
            weight_entry = tkinter.Entry(window)
            weight_entry.pack()
            
            percentage_label = tkinter.Label(window, text="10+2 Boards %:")
            percentage_label.pack()
            percentage_entry = tkinter.Entry(window)
            percentage_entry.pack()
            
            password_label = tkinter.Label(window, text="Password :")
            password_label.pack()
            password_entry=tkinter.Entry(window)
            password_entry.pack()
            
            save_button = tkinter.Button(window, text="Save", command=save_recruit_data)
            save_button.pack()
            
            window.mainloop()
        
        def summary():
            mydb = mysql.connector.connect(host='localhost',user='Vedansh Gandharva',password='130207',database="AgniVeer")
            cursor = mydb.cursor()
            sql_select ="SELECT * FROM recruitdata"
            cursor.execute(sql_select)
            records = cursor.fetchall()
            a=len(records)
            print("Total No. of AgniVeer Recruits =",a)
            print()
            summary =""
            
            for record in records:
                name, age, qualification, height, address, weight, percentage = record
                summary += f"Name: {name}\n"
                summary += f"Age: {age}\n"
                summary += f"Qualification: {qualification}\n"
                summary += f"Height: {height}\n"
                summary += f"Address: {address}\n"
                summary += f"Weight: {weight}\n"
                summary += f"Percentage: {percentage}\n"
                summary +="-------------------------\n"
            print(summary)
        
        def filterd():
            def finddata():
                a=e1.get()
                b=e2.get()
                q="SELECT * FROM recruitdata WHERE "+a+" LIKE %s"
                c.execute(q,[b])
                r=c.fetchall()
                if r==[]:
                    b.config(text="No Record Found")
                else:
                    summary =""
                    for record in r:
                        name, age, qualification, height, address, weight, percentage = record
                        summary += f"Name: {name}\n"
                        summary += f"Age: {age}\n"
                        summary += f"Qualification: {qualification}\n"
                        summary += f"Height: {height}\n"
                        summary += f"Address: {address}\n"
                        summary += f"Weight: {weight}\n"
                        summary += f"Percentage: {percentage}\n"
                        summary +="-------------------------\n"
                    summary_window = tkinter.Toplevel()
                    summary_label = tkinter.Label(summary_window, text=summary)
                    summary_label.pack()
                    b.config(text="Record Found!")
            
            window=tkinter.Tk()
            window.title("AgniVeer Officer Filter System")
            frame=tkinter.Frame(window)
            frame.pack()
            
            aframe=tkinter.LabelFrame(frame,text="Filter")
            aframe.grid(row=0,column=0,padx=50,pady=50)
            
            l1=tkinter.Label(frame,text="Enter field to search in : ")
            l1.grid(row=1,column=0)
            e1=tkinter.Entry(frame)
            e1.grid(row=2,column=0)
            
            l2=tkinter.Label(frame,text="Enter what to search for : ")
            l2.grid(row=3,column=0)
            e2=tkinter.Entry(frame)
            e2.grid(row=4,column=0)
            
            for widgit in aframe.winfo_children():
                widgit.grid_configure(padx=10,pady=5)
            
            b=tkinter.Button(frame,text="FIND",command=finddata)
            b.grid(row=5,column=0,padx=50,pady=50)
        
        def delrec():
            def delete_record():
                name = name_entry.get()
                mydb = mysql.connector.connect(host='localhost',user='Vedansh Gandharva',password='130207',database="AgniVeer")
                cursor = mydb.cursor()
                
                sql_select ="SELECT * FROM recruitdata WHERE name = %s"
                values = (name,)
                cursor.execute(sql_select, values)
                record = cursor.fetchone()
                
                if record:
                    sql1_delete ="DELETE FROM recruitlogincred WHERE name = %s"
                    sql2_delete ="DELETE FROM recruitdata WHERE name=%s"
                    cursor.execute(sql1_delete, values)
                    cursor.execute(sql2_delete, values)
                    mydb.commit()
                    result_label.config(text="Record deleted successfully!")
                else:
                    result_label.config(text="Record not found.")
            
            window = tkinter.Tk()
            
            name_label = tkinter.Label(window, text="Name:")
            name_label.pack()
            name_entry = tkinter.Entry(window)
            name_entry.pack()
            
            delete_button = tkinter.Button(window, text="Delete", command=delete_record)
            delete_button.pack()
            
            result_label = tkinter.Label(window)
            result_label.pack()
            
            window.mainloop()
        
        def updrec():
            def update_record():
                name = name_entry.get()
                age = age_entry.get()
                qualification = qualification_entry.get()
                height = height_entry.get()
                address = address_entry.get()
                weight = weight_entry.get()
                percentage = percentage_entry.get()
                
                mydb = mysql.connector.connect(host='localhost',user='Vedansh Gandharva',password='130207',database="AgniVeer")
                cursor = mydb.cursor()
                
                sql_update ="UPDATE recruitdata SET age = %s, qualification = %s, height = %s, address = %s, weight = %s, percentage = %s WHERE name = %s"
                values = (age, qualification, height, address, weight, percentage, name)
                
                cursor.execute(sql_update, values)
                mydb.commit()
                update_button.config(text="Record updated successfully!")
            
            window = tkinter.Tk()
            
            name_label = tkinter.Label(window, text="Name:")
            name_label.pack()
            name_entry = tkinter.Entry(window)
            name_entry.pack()
            
            age_label = tkinter.Label(window, text="Age:")
            age_label.pack()
            age_entry = tkinter.Spinbox(window, from_='18', to='20')
            age_entry.pack()
            
            qualification_label = tkinter.Label(window, text="Qualification:")
            qualification_label.pack()
            qualification_entry = tkinter.Entry(window)
            qualification_entry.pack()
            
            height_label = tkinter.Label(window, text="Height:")
            height_label.pack()
            height_entry = tkinter.Entry(window)
            height_entry.pack()
            
            address_label = tkinter.Label(window, text="Address:")
            address_label.pack()
            address_entry = tkinter.Entry(window)
            address_entry.pack()
            
            weight_label = tkinter.Label(window, text="Weight:")
            weight_label.pack()
            weight_entry = tkinter.Entry(window)
            weight_entry.pack()
            
            percentage_label = tkinter.Label(window, text="Percentage:")
            percentage_label.pack()
            percentage_entry = tkinter.Entry(window)
            percentage_entry.pack()
            
            update_button = tkinter.Button(window, text="Update", command=update_record)
            update_button.pack()
            
            window.mainloop()

def reclogin():
    def dataverif():
        m=mail_entry.get()
        p=pwd_entry.get()
        q1="SELECT * FROM recruitlogincred WHERE mail=%s and pwd=%s"
        c.execute(q1,[m,p])
        r=c.fetchall()
        s=r[0][0]
        if r:
            reg()
        else:
            tkinter.messagebox.showwarning(title="Error",message="No data found!")
    
    window=tkinter.Tk()
    window.title("Welcome to AgniVeer Recruit LogIn System")
    frame=tkinter.Frame(window)
    frame.pack()
    
    user_info_frame=tkinter.LabelFrame(frame,text="User Information")
    user_info_frame.grid(row=0,column=0,padx=50,pady=50)
    
    mail_label=tkinter.Label(user_info_frame,text="Mail ID")
    mail_label.grid(row=0,column=0)
    mail_entry=tkinter.Entry(user_info_frame)
    mail_entry.grid(row=1,column=0)
    
    pwd_info_frame=tkinter.LabelFrame(frame,text="Password Information")
    pwd_info_frame.grid(row=1,column=0,padx=50,pady=50)
    
    pwd_label=tkinter.Label(pwd_info_frame,text="Password")
    pwd_label.grid(row=2,column=0)
    pwd_entry=tkinter.Entry(pwd_info_frame)
    pwd_entry.grid(row=3,column=0)
    
    for widgit in pwd_info_frame.winfo_children():
        widgit.grid_configure(padx=10,pady=5)
    
    b=tkinter.Button(frame,text="Login",command=dataverif)
    b.grid(row=5,column=0,padx=50,pady=50)
    
    def reg():
        def viewdata():
            a=(s,)
            qr="SELECT * FROM recruitdata WHERE name=%s"
            c.execute(qr,a)
            r=c.fetchall()
            summary =""
            for record in r:
                name, age, qualification, height, address, weight, percentage = record
                summary += f"Name: {name}\n"
                summary += f"Age: {age}\n"
                summary += f"Qualification: {qualification}\n"
                summary += f"Height: {height}\n"
                summary += f"Address: {address}\n"
                summary += f"Weight: {weight}\n"
                summary += f"Percentage: {percentage}\n"
                summary += "-------------------------\n"
            if summary =='':
                b3.config(text="No data found!")
            summary_window = tkinter.Toplevel()
            summary_label = tkinter.Label(summary_window, text=summary)
            summary_label.pack()
        
        m=mail_entry.get()
        p=pwd_entry.get()
        q1="SELECT name FROM recruitlogincred WHERE mail=%s and pwd=%s"
        c.execute(q1,[m,p])
        r=c.fetchall()
        #coz r is a list with tuple as element inside
        s=r[0][0]
        window=tkinter.Tk()
        window.title("Welcome "+s+" to AgniVeer Recruitment System")
        frame=tkinter.Frame(window)
        frame.pack()
        
        log_info_frame=tkinter.LabelFrame(frame)
        log_info_frame.grid(row=1,column=0,padx=50,pady=50)
        
        for widgit in log_info_frame.winfo_children():
            widgit.grid_configure(padx=10,pady=5)
        
        b1=tkinter.Button(frame,text="VIEW YOUR PROFILE",command=viewdata)
        b1.grid(row=1,column=0,padx=50,pady=50)
        
        b2=tkinter.Button(frame,text="EDIT YOUR PROFILE",command=data)
        b2.grid(row=2,column=0,padx=50,pady=50)
        
        b3=tkinter.Button(frame,text="LOG OUT",command=exit)
        b3.grid(row=3,column=0,padx=50,pady=50)
        
        def data():
            def save_recruit_data():
                name = name_entry.get()
                age = age_entry.get()
                qualification = qualification_entry.get()
                height = height_entry.get()
                address = address_entry.get()
                weight = weight_entry.get()
                percentage = percentage_entry.get()
                
                mydb = mysql.connector.connect(host='localhost',user='Vedansh Gandharva',password='130207',database="AgniVeer")
                cursor = mydb.cursor()
                
                sql_insert ="INSERT INTO recruitdata(name, age, qualification, height, address, weight, percentage) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                values = (name, age, qualification, height, address, weight, percentage)
                cursor.execute(sql_insert, values)
                mydb.commit()
                cursor.close()
                mydb.close()
                save_button.config(text="Record updated successfully!")
            
            window = tkinter.Tk()
            
            name_label = tkinter.Label(window, text="Name :")
            name_label.pack()
            name_entry = tkinter.Entry(window)
            name_entry.pack()
            
            age_label = tkinter.Label(window, text="Age :")
            age_label.pack()
            age_entry = tkinter.Spinbox(window, from_='18', to='20')
            age_entry.pack()
            
            qualification_label = tkinter.Label(window, text="Qualification :")
            qualification_label.pack()
            qualification_entry = tkinter.Entry(window)
            qualification_entry.pack()
            
            height_label = tkinter.Label(window, text="Height (in cm) :")
            height_label.pack()
            height_entry = tkinter.Entry(window)
            height_entry.pack()
            
            address_label = tkinter.Label(window, text="Address :")
            address_label.pack()
            address_entry = tkinter.Entry(window)
            address_entry.pack()
            
            weight_label = tkinter.Label(window, text="Weight (in kg) :")
            weight_label.pack()
            weight_entry = tkinter.Entry(window)
            weight_entry.pack()
            
            percentage_label = tkinter.Label(window, text="10+2 Boards % :")
            percentage_label.pack()
            percentage_entry = tkinter.Entry(window)
            percentage_entry.pack()
            
            save_button = tkinter.Button(window, text="Save", command=save_recruit_data)
            save_button.pack()
            
            window.mainloop()

def login():
    window=tkinter.Tk()
    window.title("AgniVeer LogIn System")
    frame=tkinter.Frame(window)
    frame.pack()
    
    f=tkinter.LabelFrame(frame)
    f.grid(row=0,column=0,padx=50,pady=50)
    
    for widgit in f.winfo_children():
        widgit.grid_configure(padx=10,pady=5)
    
    b1=tkinter.Button(frame,text="RECRUIT's LOGIN",command=reclogin,font=("Cambria",20,"bold"))
    b1.grid(row=1,column=0,padx=50,pady=50)
    
    b2=tkinter.Button(frame,text="OFFICER's LOGIN",command=offlogin,font=("Cambria",20,"bold"))
    b2.grid(row=2,column=0,padx=50,pady=50)
