def greet_user(username):
    """Display a simple greeting"""
    print("Hello: " + username)


# greet_user("Carl")
# greet_user("Alice")

# def get_employee_info(employee_name, employee_id=123):
#     print("Hello," + str(employee_name))
#     print("Your employee id is " + str(employee_id))
#
# # get_employee_info("jesse", 123)
# get_employee_info("carl", 567)


# def make_pizza(username, *toppings):
#     print(username)
#     print(toppings)
#
#
# make_pizza("jake", "pepperoni", "extra cheese", "green pepper")


# def get_sum(value_a, value_b):
#     return value_a + value_b
#
#
# print(get_sum(6, 8))

# temperatures = [100, 108, 88, 108, 99, 102, 101]
#
# temperatures_2 = [66, 56, 77, 45, 55, 56, 71]
#
# def get_mean(a_list):
#     """Calculate the mean of a list"""
#     total = 0
#     number_of_items = len(a_list)
#     for item in a_list:
#         total += item
#     result = total / number_of_items
#     return result
#
#
# average_tep = get_mean(temperatures_2)
# print(average_tep)

def build_person(first_name, last_name):
    person = {"first": first_name, "last": last_name}
    return person


player = build_person("kobe", "bryant")
print(player)