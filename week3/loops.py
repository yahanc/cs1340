# unconfirmed_users = ["alice", "carl", "brain"]
#
# confirmed_users = []
#
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop(0)
#     print("Verifying user:" + current_user)
#     confirmed_users.append(current_user)
#
# print(confirmed_users)

employee_info = {
    "123": {
        "name": "Joe",
        "department": "IT"
    },
    "456": {
        "name": "David",
        "department": "CS"
    },
    "789": {
        "name": "Carl",
        "department": "CS"
    }
}

retired_ids = ["456"]

while retired_ids:
    r_id = retired_ids.pop()
    print(r_id)
    del employee_info[r_id]

# print(employee_info)


a_list = [1, 2, 3, 4]