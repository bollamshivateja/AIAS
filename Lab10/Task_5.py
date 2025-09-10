def div(a,b):
    return a/b
try:
    print(div(10, 0))
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
