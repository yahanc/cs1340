import json

# data = {
#     "player": {
#         "name": "Carl",
#         "age" : 18
#     }
# }
#

numbers = [1, 2,3 , 4, 6]
filename = "numbers.json"
with open(filename, "w") as the_file:
    json.dump(numbers, the_file)

# filename = "player.json"
# with open(filename) as the_file:
#     player = json.load(the_file)
#
# print(player["player"]["name"])