import random

target_number = random.randint(1, 100)
print(target_number)
allowed_attempts = 10

attempts_made = 0

while attempts_made < allowed_attempts:
    current_guess = int(input("Please input a number:"))
    if current_guess < target_number:
        print("Too Low")
    elif current_guess > target_number:
        print("Too High")
    else:
        print("Good Job")
        break
    attempts_made += 1
