# import time

# for i in range(10):
#     print (i)

# for i in range(50,100+1, 2):
#     print (i)


# for i in "Bro Code":
#     print(i)

# for seconds in range(10,0,-1):
#     print(seconds)
#     time.sleep(1)


# print("Happy New York!")

from tkinter import *

# food = ["pizza","hamburger","hotdog"]

# def order():
#     if(x.get() == 0):
#         print("You ordered pizza!")
#     elif(x.get() == 1):
#         print("You ordered a hamburger!")
#     elif(x.get() ==2):
#         print("You ordered a hotdog!")
#     else:
#         print("huh?")

# window = Tk()

# pizzaImage = PhotoImage(file='pizza.png')
# hamburgerImage = PhotoImage(file='hamburger.png')
# hotdogImage = PhotoImage(file='hotdog.png')
# foodImages = [pizzaImage,hamburgerImage,hotdogImage]

# x = IntVar()

# for index in range(len(food)):
#     radiobutton = Radiobutton(window,
#                               text=food[index], #adds text to radio buttons
#                               variable = x, #groups radiobuttons tegether if they share the same variable
#                               value = index,  # assigns each radiobutton a different value
#                               padx = 25, #adds padding on x-axis
#                               font=("Arail",50),
#                               image=foodImages[index],
#                               compound = 'left',
#                               indicatoron=0, #eliminate circle indicators
#                               width = 375, #sets width of radio buttons
#                               command=order
#                               )
#     radiobutton.pack(anchor=W)

# window.mainloop()

# def submit():
#     print("The temperature is: "+ str(scale.get())+ " degrees C")

# window = Tk()

# hotImage = PhotoImage(file='hot.png')
# hotLabel = Label(image=hotImage)
# hotLabel.pack()

# scale = Scale(window,
#               from_=100, 
#               to = 0,
#               length=600,
#               orient=VERTICAL,
#               font = ('Consolas',20),
#               tickinterval = 10, #adds numeric indicators for value
#               #showvalue = 0, #hide current value
#               resolution = 5, # increment of slider
#               troughcolor = '#69EAFF',
#               fg = '#FF1C00',
#               bg = '#111111'
#               )

# scale.set((scale['from']-scale['to'])/2 + scale['to'])  #set current value of slider
# scale.pack()

# coldImage = PhotoImage(file='cold.png')
# coldLabel = Label(image=hotImage)
# coldLabel.pack()

# button = Button(window,text='submit',command=submit)
# button.pack()

# window.mainloop()

# listbox = A listing of selectable text items within it's own container
# window = Tk()

# def submit():
#     food = []

#     for index in listbox.curselection():
#         food.insert(index,listbox.get(index))
#     print("You have ordered: ")
#     #print(listbox.get(listbox.curselection()))
#     for index in food:
#         print(index)

# def add():
#     listbox.insert(listbox.size(), entryBox.get())
#     listbox.config(height=listbox.size())

# def delete():
#     #listbox.delete(listbox.curselection())
#     for index in reversed(listbox.curselection()):
#         listbox.delete(index)
#     listbox.config(height=listbox.size())

# listbox = Listbox(window,
#                   bg="#f7ffde",
#                   font=("Constantia",35),
#                   width=12,
#                   selectmode=MULTIPLE)
# listbox.pack()

# listbox.insert(1,"pizza")
# listbox.insert(2,"pasta")
# listbox.insert(3,"garlic bread")
# listbox.insert(4,"soup")
# listbox.insert(5,"salad")

# listbox.config(height=listbox.size())

# entryBox = Entry(window)
# entryBox.pack()

# submitButton = Button(window,text="submit",command=submit)
# submitButton.pack()

# addButton = Button(window,text="add",command=add)
# addButton.pack()

# deleteButton = Button(window,text="delete",command=delete)
# deleteButton.pack()

# window.mainloop()

from tkinter import messagebox  #import messagebox library

def click():
    #messagebox.showinfo(title = 'This is an info message box',message='You are a person')
    # while(True):
    #     messagebox.showwarning(title = 'WARNING!',message='You have A VIRUS!!!!')
    # messagebox.showerror(title='ERROR!',message='something went wrong :(')
    # if messagebox.askokcancel(title='ask ok cancel',message='Do you want to do the thing?'):
    #     print('You did a thing!')
    # else:
    #     print('You canceled a thing! :(')
    # if messagebox.askretrycancel(title='ask ok cancel',message='Do you want to retry the thing?'):
    #     print('You retried a thing!')
    # else:
    #     print('You canceled a thing! :(')
    # if messagebox.askyesno(title='ask yes or no',message='Do you like cake?'):
    #     print('I like cake too:)')
    # else:
    #     print('Why do you not like cake? :(')

    # answer = messagebox.askquestion(title='ask question',message='Do you like pie?')
    # if(answer == 'yes'):
    #     print('I like pie too :)')
    # else:
    #     print('Why do you not like pie?')

    # answer = messagebox.askyesnocancel(title=' Yes no cancel',message='Do you like to code?',icon='warning')
    # if(answer==True):
    #     print("You like to code:)")
    # elif(answer==False):
    #     print("Then why are you watching a video on coding?")
    # else:
    #     print("You have dodged the question ")


# window = Tk()

# button = Button(window,command=click,text='click me')
# button.pack()

# window.mainloop()