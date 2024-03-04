# capitals = {'USA': 'Washington DC',
#             'India': 'New Dehli',
#             'China': 'Beijing',
#             'Russia': 'Moscow'}

# capitals.update({'Germany': 'Berlin'})
# capitals.update({'USA':'Las Vegas'})
# capitals.pop('China')
# capitals.clear()

# #print(capitals['Germany'])
# #print(capitals.get('Germany'))
# #print(capitals.keys())

# for key,value in capitals.items():
#     print(key, value)

# from tkinter import *
# from tkinter.ttk import *
# import time

# def start():
#     GB = 50
#     download = 0
#     speed = 2
#     while(download<GB):
#         time.sleep(0.05)
#         bar['value']+=(speed/GB)*100
#         download+=speed
#         percent.set(str(int((download/GB)*100))+"%")
#         text.set(str(download)+"/"+str(GB)+" GB completed")
#         window.update_idletasks()

# window = Tk()

# percent = StringVar()
# text = StringVar()

# bar=Progressbar(window,orient=VERTICAL,length=300)
# bar.pack(pady=10)

# percentLabel = Label(window,textvariable=percent).pack()
# taskLabel = Label(window,textvariable=text).pack()

# button = Button(window,text="download",command=start).pack()



# window.mainloop()

# canvas = widget that is used to draw graphs, plots, images in a window

# from tkinter import *

# window = Tk()

# canvas = Canvas(window,height=500,width=500)
# # canvas.create_line(0,0,500,500,fill="blue",width=5)
# # canvas.create_line(0,500,500,0,fill="red",width=5)
# # canvas.create_rectangle(50,50,250,250,fill="purple")
# # points = [250,0,500,500,0,500]
# # canvas.create_polygon(points,fill="yellow",outline="black",width=5)
# # canvas.create_arc(0,0,500,500,style=PIESLICE,start=270,extent=180)
# canvas.create_arc(0,0,500,500,fill="red",extent=180,width=10)
# canvas.create_arc(0,0,500,500,fill="white",extent=180,start=180,width=10)
# canvas.create_oval(190,190,310,310,fill="white",width=10)
# canvas.pack()


# window.mainloop()

# from tkinter import *

# def doSomething(event):
#     # print("You pressed: " + event.keysym)
#     label.config(text=event.keysym)

# window = Tk()

# window.bind("<Key>",doSomething)

# label = Label(window,font=("Helvetica",100))
# label.pack()

# window.mainloop()

# from tkinter import *

# def doSomething(event):
#     print("Mouse coordinates: " + str(event.x)+","+str(event.y))

# window = Tk()

# # window.bind("<Button-1>",doSomething)  #left mouse click
# # window.bind("<Button-2>",doSomething)  #scroll wheel
# # window.bind("<Button-3>",doSomething)  #right mouse click
# # window.bind("<ButtonRelease>",doSomething)
# # window.bind("<Enter>",doSomething)  #enter the window
# # window.bind("<Leave>",doSomething) #leave the window
# window.bind("<Motion>",doSomething)  #Where the mouse moved

# window.mainloop()

# from tkinter import *

# def drag_start(event):
#     widget = event.widget
#     widget.startX = event.x
#     widget.startY = event.y

# def drag_motion(event):
#     widget = event.widget
#     x = widget.winfo_x() - widget.startX + event.x
#     y = widget.winfo_y() - widget.startY + event.y
#     widget.place(x=x,y=y)

# window = Tk()

# label = Label(window,bg="red",width=10,height=5)
# label.place(x=0,y=0)

# label2 = Label(window,bg="blue",width=10,height=5)
# label2.place(x=100,y=100)

# label.bind("<Button-1>",drag_start)
# label.bind("<B1-Motion>",drag_motion)

# label2.bind("<Button-1>",drag_start)
# label2.bind("<B1-Motion>",drag_motion)

# window.mainloop()

# from tkinter import *

# def move_up(event):
#     label.place(x=label.winfo_x(), y=label.winfo_y()-10)

# def move_down(event):
#     label.place(x=label.winfo_x(), y=label.winfo_y()+10)

# def move_left(event):
#     label.place(x=label.winfo_x()-10, y=label.winfo_y())

# def move_right(event):
#     label.place(x=label.winfo_x()+10, y=label.winfo_y())

# window = Tk()
# window.geometry("500x500")

# window.bind("<w>",move_up)
# window.bind("<s>",move_down)
# window.bind("<a>",move_left)
# window.bind("<d>",move_right)
# window.bind("<Up>",move_up)
# window.bind("<Down>",move_down)
# window.bind("<Left>",move_left)
# window.bind("<Right>",move_right)

# myimage = PhotoImage(file='racecar.png')
# label = Label(window,image=myimage,bg="red")
# label.place(x=0,y=0)

# window.mainloop()

# from tkinter import *
# import time

# WIDTH = 500
# HEIGHT = 500
# xVelocity = 3
# yVelocity = 2

# window = Tk()

# canvas = Canvas(window,width=WIDTH,height=HEIGHT)
# canvas.pack()

# background_photo = PhotoImage(file='space.png')
# background = canvas.create_image(0,0,image=background_photo,anchor=NW)

# photo_image = PhotoImage(file='ufo.png')
# my_image = canvas.create_image(0,0,image=photo_image,anchor=NW)

# image_width = photo_image.width()
# image_height = photo_image.height()

# while True:
#     coordinates = canvas.coords(my_image)
#     print(coordinates)
#     if(coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0):
#         xVelocity = -xVelocity
#     if(coordinates[1]>=(HEIGHT-image_height) or coordinates[1]<0):
#         yVelocity = -yVelocity
#     canvas.move(my_image,xVelocity,yVelocity)
#     window.update()
#     time.sleep(0.01)

# window.mainloop()

# from tkinter import *
# from Ball import *
# import time

# window = Tk()

# WIDTH = 500
# HEIGHT = 500

# canvas = Canvas(window,width=WIDTH,height=HEIGHT)
# canvas.pack()

# volley_ball = Ball(canvas,0,0,100,1,1,"white")
# tennis_ball = Ball(canvas,0,0,50,4,3,"yellow")
# basket_ball = Ball(canvas,0,0,125,8,7,"orange")

# while True:
#     volley_ball.move()
#     tennis_ball.move()
#     basket_ball.move()
#     window.update()
#     time.sleep(0.01)

# window.mainloop()

from tkinter import *
from time import *

def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    time_label.after(1000,update)

window = Tk()

time_label = Label(window,font=("Arial",50),fg="#00FF00",bg="black")
time_label.pack()

day_label = Label(window,font=("Ink Free",25))
day_label.pack()

date_label = Label(window,font=("Ink Free",30))
date_label.pack()

update()

window.mainloop()
