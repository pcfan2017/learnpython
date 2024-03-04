import os
path = "/home/ubuntu/learnpython/check.ping"

if os.path.exists(path):
    print("That location exists!")
else:
    print("That location doesn't exist!")

try:
    with open('check1.ping') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")