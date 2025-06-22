import math

num = float(input("Enter a number: "))
rounded = math.ceil(num)
print(str(rounded).replace(",",""))