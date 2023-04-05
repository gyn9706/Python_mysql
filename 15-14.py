from tkinter import *

window=Tk()

window.geometry("200x200")

upFrame=Frame(window)
upFrame.pack()
downFrame=Frame(window)
downFrame.pack()

editBox=Entry(upFrame,width=10,bg='green')
editBox.pack(padx=20,pady=20)

listbox=Listbox(downFrame,bg='yellow')
listbox.pack() 

listbox.insert(0,"하나")
listbox.insert(1,"둘")
listbox.insert(2,"셋")

window.mainloop()