number = int(input("Enter a number: "))
if number > 25:
    print("Error")
else:
    i = 1
    while i <= number:
        if i % 2 == 0:
            print(f"{i} is even")
        else:
            print(f"{i} is odd")
        i += 1