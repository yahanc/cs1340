# name = 'name'

emp_dict = {}
user_info = {
    'name': 'ethan',
    'age': 23,
    'address': {
            'state': 'TX',
            'zip': 75206
            }
}
# print(user_info['department'])
# print(user_info.get('department', 'CS'))
print(emp_dict)
emp_dict['alice'] = 1
emp_dict['carl']  = 2
emp_dict['apple'] = 3
print(emp_dict)

del emp_dict['alice']

print(emp_dict)

print(emp_dict.items())