#starter code
import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os
win = tk.Tk()
win.title('GUI')

#create labels
name_label=ttk.Label(win,text="Enter your name: ")
name_label.grid(row=0,column=0,sticky=tk.W)

email_label=ttk.Label(win,text="Enter your email: ")
email_label.grid(row=1,column=0,sticky=tk.W)

age_label=ttk.Label(win, text="Enter your age: ")
age_label.grid(row=2,column=0,sticky=tk.W)

gender_label=ttk.Label(win,text="select your gender")
gender_label.grid(row=3,column=0,sticky=tk.W)

#create entry box

name_var=tk.StringVar()
name_entrybox=ttk.Entry(win, width=16,textvariable=name_var)
name_entrybox.grid(row=0,column=1)
name_entrybox.focus()

email_var=tk.StringVar()
email_entrybox=ttk.Entry(win, width=16,textvariable=email_var)
email_entrybox.grid(row=1,column=1)

age_var=tk.StringVar()
age_entrybox=ttk.Entry(win, width=16,textvariable=age_var)
age_entrybox.grid(row=2,column=1)


#create combobox
gender_var=tk.StringVar()
gender_combobox=ttk.Combobox(win,width=13,textvariable=gender_var, state="readonly")
gender_combobox['values']=('Male','Female','Other')
gender_combobox.current(0)
gender_combobox.grid(row=3,column=1)

#create radio button
usertype=tk.StringVar()
rbtn1=ttk.Radiobutton(win,text="student",value='student',variable=usertype)
rbtn1.grid(row=4,column=0,sticky=tk.W)

rbtn2=ttk.Radiobutton(win,text="Teacher",value='Teacher',variable=usertype)
rbtn2.grid(row=4,column=1)

rbtn3=ttk.Radiobutton(win,text="Manager",value='Manager',variable=usertype)
rbtn3.grid(row=4,column=2)

#create check button
checkbtn_var=tk.IntVar()
checkbtn=ttk.Checkbutton(win,text="check this button to like GUI", variable=checkbtn_var)

checkbtn.grid(row=5,columnspan=3,sticky=tk.W)

#create button
# def action():
#     username=name_var.get()
#     userage=age_var.get()
#     user_email=email_var.get()
#     user_gender=gender_var.get()
#     print(f"{username} is {userage} years old and gender is {user_gender},{user_email}")
#     user_type = usertype.get()
#     if checkbtn_var.get()==0:
#         like="NO"
#     else:
#         like="YES"
#     print(user_type,like)
#
#     with open('GUI.txt','a') as f:
#         f.write(f'{username}, {userage}, {user_email}, {user_gender}, {user_type}, {like}\n')
#     name_entrybox.delete(0,tk.END)
#     age_entrybox.delete(0, tk.END)
#     email_entrybox.delete(0, tk.END)
#     name_label.configure(foreground="#b388ff")

    # submit_button.configure(foreground="Blue")
def action():
    username = name_var.get()
    userage=age_var.get()
    user_email=email_var.get()
    user_type = usertype.get()
    user_gender=gender_var.get()
    if checkbtn_var.get()==0:
        like="NO"
    else:
        like="YES"
     #write csv file:
    with open('GUI2.csv','a',newline='') as f:
        dict_writer=DictWriter(f,fieldnames=['userName','user Email','user age','user gender','user type','like'])
        if os.stat('GUI2.csv').st_size==0:
            dict_writer.writeheader()
        dict_writer.writerow({'userName':username,
                              'user Email':user_email,
                              'user age':userage,
                              'user gender':user_gender,
                              'user type':user_type,
                              'like':like})

    name_entrybox.delete(0, tk.END)
    age_entrybox.delete(0, tk.END)
    email_entrybox.delete(0, tk.END)

submit_button=tk.Button(win,text="submit", command=action)
submit_button.grid(row=6,column=0)

win.mainloop()