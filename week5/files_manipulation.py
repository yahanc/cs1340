
file_name = "dem0.txt"
try:
    with open(file_name) as file_object:
        contents = file_object.readline()
        print(contents)
        data = contents.split(",")
        print(float(data[-1]))
    x = 18
    y = 0
    z = x / y
except FileNotFoundError:
    print("something went wrong")
except ZeroDivisionError:
    print("You can not divide a number by zero")
except NameError:
    print("Check undefined variables")


