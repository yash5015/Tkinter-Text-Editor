import tkinter as tk
from tkinter import ttk
win=tk.Tk()
win.title('LOOP')

labels=["What is your name: ","What is your age: ","What is your gender: ","Country:","state:","city:","address:"]
#labels
for i in range(len(labels)):
    cur_label="label"+str(i)
    cur_label=ttk.Label(win,text=labels[i])
    cur_label.grid(row=i,column=0,sticky=tk.W,padx=2,pady=2)
#entry box

user_info={
    "name": tk.StringVar(),
    'age': tk.StringVar(),
    'gender': tk.StringVar(),
    'country': tk.StringVar(),
    'state': tk.StringVar(),
    'city': tk.StringVar(),
    'address':tk.StringVar()
}
counter=0
for i in user_info:
    cur_entrybox='entry'+i
    cur_entry = ttk.Entry(win, width=16, textvariable=user_info[i])
    cur_entry.grid(row=counter, column=1,padx=2,pady=2)
    counter+=1
def submit():
    print(user_info['name'].get())
    print(user_info.get('age').get())
    print(user_info.get('gender').get())
    print(user_info.get('country').get())
    print(user_info.get('state').get())
    print(user_info.get('city').get())
    print(user_info.get('address').get())

submit_btn=ttk.Button(win,text="Submit",command=submit)
submit_btn.grid(row=7,column=0,sticky=tk.W)



win.mainloop()