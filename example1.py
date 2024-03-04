# print("I love pizza.")
# print("It is really good!")

# name = "Bro"
# print(name)

# name = input("What is your name?: ")
# age = int(input("How old are you?: "))
# height = float(input("How tall are you?: "))

# print("Hello " + name)
# print("You are " + str(age)+" years old")
# print("You are "+ str(height)+"cm tall")

# import time

# print(time.ctime(1000000))
# print(time.time())
# print(time.ctime(time.time()))
# time_object = time.localtime()
# print(time_object)
# local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
# print(local_time)

# time.strptime


# thread
# io bound
# cpu bound

# import threading
# import time

# def eat_breakfast():
#     time.sleep(3)
#     print("You eat breakfast")

# def drink_coffee():
#     time.sleep(4)
#     print("You drank coffee")

# def study():
#     time.sleep(5)
#     print("You finish studying")

# x = threading.Thread(target=eat_breakfast, args=())
# x.start()

# y = threading.Thread(target=drink_coffee, args=())
# y.start()

# z = threading.Thread(target=study, args=())
# z.start()

# # eat_breakfast()
# # drink_coffee()
# # study()
# x.join()
# y.join()
# z.join()
# print(threading.active_count())
# print(threading.enumerate())
# print(time.perf_counter())

# daemon thread = a thread that runs in the background, ex. background tasks, garbage collection, waiting for input, long running process
# import threading
# import time

# def timer():
#     print()
#     count = 0
#     while True:
#         time.sleep(1)
#         count += 1
#         print("logged in for: ", count, "seconds")

# x = threading.Thread(target=timer, daemon=True)
# x.start()

# answer = input("Do you wish to exist?")

# Python multiprocessing
from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():

    print(cpu_count())
    a = Process(target=counter, args=(250000000,))
    b = Process(target=counter, args=(250000000,))
    c = Process(target=counter, args=(250000000,))
    d = Process(target=counter, args=(250000000,))

    # a.start()
    # b.start()
    # c.start()
    # d.start()

    # a.join()
    # b.join()
    # c.join()
    # d.join()

    print("finished in:", time.perf_counter(), "seconds")

if __name__ == '__main__':
    main()