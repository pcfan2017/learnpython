name = "Bro"


def hello(**kwargs):
    print("Hello",end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")

hello(first="Bro", middle="Dude", last="Code")

animal = 'cow'
item = "moon"

print("The {} jumped over the {}".format(item,animal))
print("The {1} jumped over the {1}".format(item,animal))

name = "this"
print("Hello, my name is {:^10}. Nice to meet you".format(name))
