import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box
win=tk.Tk()
win.title('Message_Box')
#label Frame

label_frame=ttk.LabelFrame(win,text='Contact Details:')
label_frame.grid(row=0,column=0,padx=40,pady=10)

#label
name_label=ttk.Label(label_frame,text="Enter your name: ",font=('Helvetica',14))
age_label=ttk.Label(label_frame,text="Enter your age: ",font=('Helvetica',14))

#entry box variable
name_var=tk.StringVar()
age_var=tk.StringVar()

#entry boxes
name_entry=ttk.Entry(label_frame,width=36,textvariable=name_var)
age_entry=ttk.Entry(label_frame,width=36,textvariable=age_var)

#grid
name_label.grid(row=0,column=0,padx=5,pady=5,sticky=tk.W)
age_label.grid(row=0,column=1,padx=5,pady=5,sticky=tk.W)
name_entry.grid(row=1,column=0,padx=5,pady=5,sticky=tk.W)
age_entry.grid(row=1,column=1,padx=5,pady=5,sticky=tk.W)

#submit button
def submit():
    # m_box.showinfo('title','content of this message box!!')
    name=name_var.get()
    age=age_var.get()
    if name=="" or age=="":
        m_box.showerror('Error',"Please fill above details:")
    else:
        try:
            age=int(age)
        except ValueError:
            m_box.showerror('Error','only digits are accepted in age box')
        else:
            if age<18:
                m_box.showwarning('warning','you are not above 18, visit this content at your own risk')
            print(f'{name} is {age} years old')


submit_btn=ttk.Button(win,text="Submit",command=submit)
submit_btn.grid(row=1,column=0,padx=40)
win.mainloop()
