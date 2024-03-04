ccfile = open("/home/ubuntu/learnpython/check.ping", "r")

for aline in ccfile:
    print("ping  -c 4 " + aline)