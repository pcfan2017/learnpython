# name = "bro Code"

# #if(name[0].islower()):
# #    name = name.capitalize()

# first_name = name[0:3].upper()
# last_name = name[4:].lower()

# print(first_name)
# print(last_name)

# import smtplib
# sender = "sender@gmail.com"
# receiver = "receiver@gmail.com"
# password = "password123"
# subject = "Python email test"
# body = "I wrote an email! :D"

# # header
# message = f"""From: Snoop Dogg{sender}
# To: Nicholas Cage{receiver}
# Subject: {subject}\n
# {body}
# """

# server = smtplib.SMTP("smtp.gmail.com", 587)
# server.starttls()

# try:
#     server.login(sender,password)
#     print("Logged in ....")
#     server.sendmail(sender,receiver,message)
#     print("Email has been sent!")
# except smtplib.SMTPServerDisconnected:
#     print("unable to sing in")

# *****************************************
# run .py file with cmd
# *****************************************
# save file as .py (Python file)
# go to command prompt
# navigate to directory w/ your file: cd C:\Users\BroCode\Desktop
# invoke python interpreter + script: python hello_world.py

# print("Hello World!")

# name = input("What's your name?: ")

# print("Hello" +name)

print("Hello World")

name = input("What's your name?: ")

print("Hello " + name)