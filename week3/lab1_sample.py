accumulated_rewards = {
    "jack": {
        "points": 1,
        "level": "silver"
    },
    "ben": {
        "points": 19,
        "level": "gold"
    }
}

user_name = "Alan"
age = 54
height = 6.1
is_vegetarian = True
preferred_toppings = ["onion", "mushrooms"]

# Create a new customer
customers = []

customer_1 = {
    "name": user_name,
    "age" : age,
    "height": height,
    "is_vegetarian": is_vegetarian,
    "preferred_toppings": preferred_toppings
}

customer_2 = {
    "name": "ben",
    "age" : 18,
    "height": 6.3,
    "is_vegetarian": False,
    "preferred_toppings": ["pepperoni", "cheese"]
}

customers.append(customer_1)
customers.append(customer_2)

# Process purchases
while customers:
    current_customer = customers.pop(0)
    current_customer_name = current_customer["name"]
    print("processing customer: " + current_customer_name)

    # Updating the rewards for customer
    if current_customer_name in accumulated_rewards:
        accumulated_rewards[current_customer_name]["points"] +=1
        if accumulated_rewards[current_customer_name]["points"] < 10:
            accumulated_rewards[current_customer_name]["level"] = "silver"
        elif accumulated_rewards[current_customer_name]["points"] >= 10 and \
            accumulated_rewards[current_customer_name]["points"] < 20:
            accumulated_rewards[current_customer_name]["level"] = "gold"
        else:
            accumulated_rewards[current_customer_name]["level"] = "diamond"
    else:
        accumulated_rewards[current_customer_name] = {
            "points":1,
            "level": "silver"
        }

print(accumulated_rewards)




