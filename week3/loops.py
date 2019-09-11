# unconfirmed_users = ["alice", "carl", "brain"]
#
# confirmed_users = []
#
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop(0)
#     print("Verifying user:" + current_user)
#     confirmed_users.append(current_user)
# #
# # print(confirmed_users)
#
# employee_info = {
#     "123": {
#         "name": "Joe",
#         "department": "IT"
#     },
#     "456": {
#         "name": "David",
#         "department": "CS"
#     },
#     "789": {
#         "name": "Carl",
#         "department": "CS"
#     }
# }
#
# retired_ids = ["456"]
#
# while retired_ids:
#     r_id = retired_ids.pop()
#     print(r_id)
#     del employee_info[r_id]
#
# # print(employee_info)
#
#


#
# fruits = ["apple", "banana", "cherry"]
#
# st = "Hello world"
#
# total_value = 0
# for fts in a_list:
#     total_value += fts
#
# # total_calculation = 4
# # i = 0
# # while i < total_calculation:
# #     total_value += a_list[i]
# #     i += 1
#
# total_value = sum(a_list)
# print(total_value)


a_list = [1, 2, 3, 4]
# a_list[0] = a_list[0] * 2
#
# # new_list = []
# # for item in a_list:
# #     new_list.append(item * 2)
#
# new_list = [item *2 for item in a_list if item < 2]
#
# print(new_list)

# new_a_list = list(range(1, 5))
# print(new_a_list)
#
# for item in new_a_list:
#     print(item)

names = ["alice", "bob", "carl"]
ages  = [18, 30, 22]

for idx, item in enumerate(names):
    print(item)
    print(ages[idx])