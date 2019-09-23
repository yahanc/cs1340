x = 18
y = 1

try:
    z = x / y
except ZeroDivisionError:
    print("something went wrong")
else:
    print("everything is fine")
finally:
    print("This line will run regardless what happened")

print("This line will be executed")