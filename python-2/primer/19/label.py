import tkinter

top = tkinter.Tk()

label = tkinter.Label(top,text="input")
label.pack()

button = tkinter.Button(top,text="QIUT",command=top.quit,bg="red",fg="white")
button.pack(fill=tkinter.X,expand=1)

tkinter.mainloop()
