import math

num = float(input("Enter a number: "))
rounded = int(num) if num == int(num) else int(num) + 1
print(rounded)