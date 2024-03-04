# import math
# pi = 3.14
# x = 1
# y = 2
# z = 3

# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(abs(pi))
# print(pow(pi,2))
# print(math.sqrt(420))
# print(max(x,y,z))
# print(min(x,y,z))

# website1 = "http://google.com"
# website2 = "http://wikipedia.com"

# slice = slice(7,-4)

# print(website1[slice])
# print(website2[slice])

from tkinter import *

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

# window = Tk() # instantiate an instance of a window
# window.geometry("420x420")
# window.title("Bro Code first GUI program")

# icon = PhotoImage(file='logo.png')
# window.iconphoto(True,icon)
# window.config(background="#5cfcff")

# window.mainloop() #place window on computer screen. listen for events

#label = an area widget that holds text and/or an image within a window
# window = Tk()

# photo = PhotoImage(file='logo.png')
# label = Label(window,
#               text="Hello World",
#               font=('Arial',40,"bold"),
#               fg='green',
#               bg='black',
#               relief=RAISED,
#               bd=10,
#               padx=20,
#               pady=20,
#               image=photo,
#               compound='bottom')
# label.pack()
# #label.place(x=0,y=0)
# window.mainloop()
# count = 0

# def click():
#     global count
#     count += 1
#     print(count)

# window = Tk()

# photo = PhotoImage(file='button.png')
# button = Button(window,
#                 text="click me!",
#                 command=click,
#                 font=("Comic Sans",30),
#                 fg="#00FF00",
#                 bg="black",
#                 activeforeground="#00FF00",
#                 activebackground="black",
#                 state=ACTIVE,
#                 image=photo,
#                 compound='bottom')
# button.pack()

# window.mainloop()
# def submit():
#     username = entry.get()
#     print("Hello " + username)
#     # entry.config(state=DISABLED)

# def delete():
#     entry.delete(0,END)

# def backspace():
#     entry.delete(len(entry.get())-1, END)

# window = Tk()

# entry = Entry(window,
#               font=("Arial",50),
#               fg="#00FF00",
#               bg="black",
#               show="*")
# # entry.insert(0,'Spongebob')
# entry.pack(side=LEFT)

# submit_button = Button(window,text="submit",command=submit)
# submit_button.pack(side=RIGHT)

# delete_button = Button(window,text="delete",command=delete)
# delete_button.pack(side=RIGHT)

# backspace_button = Button(window,text="backspace",command=backspace)
# backspace_button.pack(side=RIGHT)

# window.mainloop()
def display():
    if(x.get()==1):
        print("You agree!")
    else:
        print("You don't agree:(")

window = Tk()

x = IntVar()

python_photo = PhotoImage(file='python.png')
check_button = Checkbutton(window,
                           text="I agree to something",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=('Arial',20),
                           fg='#00FF00',
                           bg='black',
                           activeforeground='#00FF00',
                           activebackground='black',
                           padx=25,
                           pady=10,
                           image=python_photo,
                           compound="left")

check_button.pack()
window.mainloop()