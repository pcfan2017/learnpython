# dictionary comprehension = created dictionaris using an expression
#                            can replace for loops and certain lambda functions
# dictionary = {key: expression for (key,value) in iterable}
# dictionary = {key: expression for (key,value) in iterable if conditional}
# dictionary = {key: (if/else) for (key,value) in iterable}
# dictionary = {key: function(value) for (key,value) in iterable}
#--------------------------------------------------------------------------
# cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
# cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
# print(cities_in_C)

#--------------------------------------------------------------------------
# weather = {'New York': "snowing", 'Boston': "sunny", 'Los Angeles': "sunny", 'Chicago': "cloudy"}
# sunny_weather = {key: value for (key,value) in weather.items() if value == "sunny"}
# print(sunny_weather)
# cities = {'New York':32, 'Boston':75,'Los Angeles':100,'Chicago':50}
# desc_cities = {key: ("WARM" if value >= 40 else "COLD") for (key,value) in cities.items()}
# print(desc_cities)

# def check_temp(value):
#     if value >= 70:
#         return "HOT"
#     elif 69>= value >=40:
#         return "WARM"
#     else:
#         return "COLD"

# cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
# desc_cities = {key: check_temp(value) for (key,value) in cities.items()}
# print(desc_cities)

# zip(*iterables) = aggregate elements from two or more iterables (list, tuples, sets, etc.)
#                   creates a zip object with paired elements stored in tuples for each element

# usernames = ["Dude", "Bro", "Mister"]
# passwords = ("p@ssword", "abc123", "guest")
# login_date = ["1/1/2012", "1/2/2021", "1/3/2021"]

# users = zip(usernames, passwords)
# print(type(users))
# for i in users:
#     print(i)

# users = dict(zip(usernames, passwords))
# print(type(users))
# for key,value in users.items():
#     print(key+" : "+value)
# users = zip(usernames, passwords,login_date)

# for i in users:
#     print(i)

# Python interpreter sets "special variables", one of which is __name__
# Python will assign the __name__ variable a value of "__main__" if it's
# the initial module being run

print(__name__)
def main():
    print("hello!")

if __name__ == '__main__':
    main()