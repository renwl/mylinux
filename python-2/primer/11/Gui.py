
from functools import partial
import tkinter

root=tkinter.Tk()
MyButton = partial(tkinter.Button,root,
                   fg="white",bg="blue")
b1= MyButton(text="button 1")
b2=MyButton(text="button 2")
#qb=MyButton(text="QUIT",bg="red",
 #           command=root.quit)

b1.pack()
b2.pack()
#qb.pack(file=Tkinter.X,expand= True)
root.title("PFAs!")
root.mainloop()
