a_list = [1, 3, 4, 39, 5, 6, 10, 19]

def look_for_number(a_list, target_number):
    l = len(a_list)
    i = 0
    while i < l:
        if a_list[i] == target_number:
            return "Found"
        i += 1
    return "Not Found"

# results = look_for_number(a_list, 10)
# print(results)

# employee = {
#     "name": "carl",
#     "age" : 23,
#     "department": "IT"
# }
#
# for k in employee.keys():
#     print(k)


m = 0

for n in a_list:
    if n >= 10:
        m += n
print(m)