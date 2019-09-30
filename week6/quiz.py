# i = 1
# while True:
#     if i % 3 == 0:
#         break
#     print(i)
#     i += 1

# employee = {
#     "name": "carl",
#     "age" : 18
# }
#
# print("department" in employee)


def build_person(first_name, last_name):
    return {
        "first": first_name,
        "last" : last_name
    }

one_person = build_person("john", "hello")
print(one_person)