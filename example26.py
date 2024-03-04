# happy = True
# print(happy)

#print(happy := True)

# foods = list()
# while food := input("What food do you like?: ") != "quit":
#     foods.append(food)

# def hello():
#     print("Hello")

# hi = hello
# hello()
# hi()

# say = print
# say("Whoa! I can't believe thsi works! :O")

# Higher order Function
# def loud(text):
#     return text.upper()

# def quiet(text):
#     return text.lower()

# def hello(func):
#     text = func("Hello")
#     print(text)

# hello(loud)
# hello(quiet)

# def divisor(x):
#     def dividend(y):
#         return y / x
#     return dividend

# divide = divisor(2)
# print(divide(10))

# lambda function
# double = lambda x: x * 2
# multiply = lambda x, y: x * y
# add = lambda x, y, z: x + y + z
# full_name = lambda first_name, last_name: first_name+" "+last_name
# age_check = lambda age: True if age >= 18 else False
# print(age_check(18))
            
# sort method
# students = ("Squidward","Sandy","Patrick","Spongebob","Mr. Krabs")
#students.sort(reverse=True)
# sorted_students = sorted(students,reverse=True)
# for i in sorted_students:
#     print(i)
# students = (("Squidward", "F", 60),
#             ("Sandy", "A", 33),
#             ("Patrick","D", 36),
#             ("Spongebob","B", 20),
#             ("Mr. Krabs","C",78))

# # grade = lambda grades:grades[1]
# age = lambda ages:ages[2]
# # students.sort(key=age,reverse=True)
# sorted_students = sorted(students,key=age)

# for i in sorted_students:
#     print(i)


# map(function,iterable)
# store = [("shirt",20.00),
#          ("pants",25.00),
#          ("jacket",50.00),
#          ("socks",10.00)]


# to_euros = lambda data:(data[0],data[1]*0.82)
# to_dollars = lambda data:(data[0],data[1]/0.82)
# #store_euros = list(map(to_euros,store))
# store_dollars = list(map(to_dollars,store))
# #print(store_euros)
# for i in store_dollars:
#     print(i)

# filter() creates a collection of elements from an iterable for which a function returns
# filter(function, iterable)
# friends = [("Rachel",19),
#            ("Monica",18),
#            ("Phoebe",17),
#            ("Joey",16),
#            ("Chandler",21),
#            ("Ross",20)]
# age = lambda data:data[1]>=18

# drinking_buddies = list(filter(age, friends))

# for i in drinking_buddies:
#     print (i)

# reduce(function, iterable) apply a function to an iterable and reduce it to a single cumulative value. 
# Performs function on first two elements and repeats process until 1 value reamins.

# import functools
# letters = ["H","E","L","L","O"]
# word = functools.reduce(lambda x, y,:x+y,letters)
# print(word)

# factorial = [5,4,3,2,1]
# result = functools.reduce(lambda x,y,:x * y, factorial)
# print(result)

# list comprehension = a way to create a new list with less syntax
#                      can mimic certain lambda functions, easier to read
#                      list = [expression for item in iterable]
#                      list = [expression for item in iterable if conditional]
#                      list = [expression if/else for item in iterable]

squares = []
for i in range(1,11):
    squares.append(i * i)
print(squares)

squares = [i * i for i in range(1,11)]
print(squares)

students = [100,90,80,70,60,50,40,30,0]
#passed_students = list(filter(lambda x: x>= 60, students))
#passed_students = [i for i in students if i >= 60]
passed_students = [i if i>= 60 else "FAILED" for i in students]
print(passed_students)