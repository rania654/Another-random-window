from tkinter import *
root = Tk()

root.geometry("500x500")
root.title("Another random window")

label=Label(root,text = "Pick a template", background = "purple")
label.pack()

entry = Entry(root, width=50)
entry.pack()

label=Label(root,text = "Name your project", background = "blue")
label.pack()

entry = Entry(root, width=50)
entry.pack()

btn = Button(root, text = "Create project", background = "pink", bd = 7)
btn.pack()




root.mainloop()