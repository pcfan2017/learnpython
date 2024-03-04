#calculate_to_unit = 24
#name_of_unit = "hours"
from helper import validate_and_execute, user_input_message

def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "unsupported unit"
   

#def scope_check(num_of_days):
#    my_var = "variable inside function"
#    print(name_of_unit)
#    print(num_of_days)
#    print(my_var)

#scope_check(20) 

#my_var = days_to_units(20)
#print(my_var)


user_input = ""    
while user_input != "exit":
    #user_input = input("Hey user, enter a number of days and I will convert it to hours!\n")
    #list_of_days = user_input.split(", ")
    #print(list_of_days)
    #print(set(list_of_days))

    #print(type(list_of_days))
    #print(type(set(list_of_days)))
    user_input = input(user_input_message)
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dictionary)
    print(type(days_and_unit_dictionary))
    validate_and_execute(days_and_unit_dictionary)
    #for num_of_days_element in user_input.split(", "):
    #    validate_and_execute()

my_list = ["20", "30", "100"]
print(my_list[2])

my_dictionary = {"days":20, "unit": "hours", "message": "all good"}
print(my_dictionary["message"])

message = "enter some value"
days = 20
price = 9.99
valid_number = True
exit_input = False
list_of_days = [20, 40, 20, 100]
list_of_months = ["January", "February", "June"]
set_of_days = {20, 45, 100}
days_and_unit = {"days": 10, "unit": "hours"}