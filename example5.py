# student = ("Bro", 21, "male")

#print(student.count("Bro"))
#print(student.index("male"))



# utensils = {"fork", "spoon", "knife", "spoon"}
# dishes = {"bowl", "plate", "cup", "knife"}

#utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear()
#utensils.update(dishes)
#dinner_table = utensils.union(dishes)

#for x in dinner_table:
#    print(x)

# print(utensils.difference(dishes))
# print(dishes.difference(utensils))

# from tkinter import *
# from tkinter import colorchooser

# def click():
#     color = colorchooser.askcolor()
#     # print(color)
#     # colorHex = color[1]
#     # print(colorHex)
#     window.config(bg=color[1]) # change background color


# window=Tk()
# window.geometry("420x420")
# button = Button(text='click me',command=click)
# button.pack()
# window.mainloop()

# text widget = functions like a text area, you can enter multiple lines of text
# from tkinter import *

# def submit():
#     input = text.get("1.0", END)
#     print(input)

# window = Tk()
# text = Text(window,
#             bg="light yellow",
#             font=("Ink Free",25),
#             height=8,
#             width=20,
#             padx=20,
#             pady=20,
#             fg="purple")

# text.pack()
# button = Button(window,text="submit",command=submit)
# button.pack()
# window.mainloop()

# from tkinter import *
# from tkinter import filedialog

# def openFile():
#     filepath = filedialog.askopenfilename(initialdir="/home/ubuntu/coffeetime",
#                                           title="Open file okay?",
#                                           filetypes=(("text files","*.txt"),
#                                           ("all files","*.*")))
#     # print(filepath)
#     file = open(filepath,"r")
#     print(file.read())
#     file.close()

# window = Tk()
# button = Button(text="Open",command=openFile)
# button.pack()
# window.mainloop()

# from tkinter import *
# from tkinter import filedialog

# def saveFile():
#     file = filedialog.asksaveasfile(initialdir="/home/ubuntu/learnpython",
#                                     defaultextension='.txt',
#                                     filetypes=[
#                                         ("Text file",".txt"),
#                                         ("HTML file",".html"),
#                                         ("All files",".*"),
#                                     ])
#     if file is None:
#         return
    
#     filetext = str(text.get(1.0,END))
#     #filetext = input("Enter some text I guess: ")
#     file.write(filetext)
#     file.close()

# window = Tk()
# button = Button(text='save',command=saveFile)
# button.pack()
# text = Text(window)
# text.pack()
# window.mainloop()

# from tkinter import *

# def openFile():
#     print("File has been opened!")
# def saveFile():
#     print("File has been saved!")
# def cut():
#     print("You cut some text!")
# def copy():
#     print("You copied some text!")
# def paste():
#     print("You pasted some text!")


# window = Tk()

# openImage = PhotoImage(file="file.png")
# saveImage = PhotoImage(file="save.png")
# exitImage = PhotoImage(file="exit.png")

# menubar = Menu(window)
# window.config(menu=menubar)

# fileMenu = Menu(menubar,tearoff=0,font=("MV Boli",15))
# menubar.add_cascade(label="File",menu=fileMenu)
# fileMenu.add_command(label="Open",command=openFile,image=openImage,compound='left')
# fileMenu.add_command(label="Save",command=saveFile,image=saveImage,compound='left')
# fileMenu.add_separator()
# fileMenu.add_command(label="Exit",command=quit,image=exitImage,compound='left')

# editMenu = Menu(menubar,tearoff=0,font=("MV Boli",15))
# menubar.add_cascade(label="Edit",menu=editMenu)
# editMenu.add_command(label="Cut",command=cut)
# editMenu.add_command(label="Copy",command=copy)
# editMenu.add_command(label="Paste",command=paste)

# window.mainloop()

# from tkinter import *

# window = Tk()

# frame = Frame(window,bg="pink",bd=5,relief=SUNKEN)
# frame.place(x=100,y=100)

# button = Button(frame,text="W",font=("Consolas",25),width=3).pack(side=TOP)
# button = Button(frame,text="A",font=("Consolas",25),width=3).pack(side=LEFT)
# button = Button(frame,text="S",font=("Consolas",25),width=3).pack(side=LEFT)
# button = Button(frame,text="D",font=("Consolas",25),width=3).pack(side=LEFT)


# window.mainloop()

# from tkinter import *

# def create_window():
#     #new_window = Toplevel()   #Toplevel() = new window 'on top' of other windows
#     new_window = Tk()       #Tk() = new independent window
#     old_window.destroy()    #close out of old

# old_window = Tk()

# Button(old_window,text="create new window",command=create_window).pack()

# old_window.mainloop()

# from tkinter import *
# from tkinter import ttk

# window =Tk()

# notebook = ttk.Notebook(window) #widget that manages a collection of windows/displays

# tab1 = Frame(notebook) #new frame for tab 1
# tab2 = Frame(notebook) #new frame for tab 2

# notebook.add(tab1,text="Tab 1")
# notebook.add(tab2,text="Tab 2")
# notebook.pack(expand=True,fill="both")  #expand = expand to fill any space not otherwise used
#                                         #fill = fill space on x and y axis

# Label(tab1,text="Hello, this is tab#1",width=50,height=25).pack()
# Label(tab2,text="Goodbye, this is tab#2",width=50,height=25).pack()

# window.mainloop()

from tkinter import *

#grid() = geometry manager that organized widgets in a table-like structure in a parent

window = Tk()

titleLabel = Label(window,text="Enter your info",font=("arial",25)).grid(row=0,column=0,columnspan=2)

firstNameLabel = Label(window,text="First name: ",width=20,bg="red").grid(row=1,column=0)
firstNameEntry = Entry(window).grid(row=1,column=1)

lastNameLabel = Label(window,text="Last name: ",bg="green").grid(row=2,column=0)
lastNameEntry = Entry(window).grid(row=2,column=1)

emailLabel = Label(window,text="email: ",bg="blue").grid(row=3,column=0)
emailEntry = Entry(window).grid(row=3,column=1)

submitButton = Button(window,text="Submit").grid(row=4,column=0)

window.mainloop()