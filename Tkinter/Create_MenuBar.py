import tkinter as tk
from tkinter import ttk
win=tk.Tk()
win.title('MenuBar')
def func():
    print("func called")


# *******************************SIMPLE MENUBAR****************************
# menubar = tk.Menu(win)
# menubar.add_command(label='Save',command=func)
# menubar.add_command(label='Save As',command=func)
# menubar.add_command(label='Open',command=func)
# menubar.add_command(label='Print',command=func)

main_menu=tk.Menu(win)
#file Menu
file_menu=tk.Menu(main_menu,tearoff=0)
file_menu.add_command(label='New File',command=func)
file_menu.add_command(label='New Folder',command=func)
file_menu.add_separator()
file_menu.add_command(label='Save',command=func)
file_menu.add_command(label='Open',command=func)

#edit Menu
edit_menu=tk.Menu(main_menu,tearoff=0)
edit_menu.add_command(label="Undo",command=func)
edit_menu.add_command(label="Redo",command=func)
edit_menu.add_command(label="Delete",command=func)
edit_menu.add_command(label="Select All",command=func)


main_menu.add_cascade(label='File',menu=file_menu)
main_menu.add_cascade(label='Edit',menu=edit_menu)

win.config(menu=main_menu)

win.mainloop()