# if __name__ == '__main__'
# **********************************************************************

# Python interpreter sets "special variables", one of which is __name__
# Python will assign the __name__ variable a value of "__main__" if it's
# the initial module being run

def hello():
    print("Hello!")

if __name__ == '__main__':
    hello()
else:
    print("runing other module indirectly")