import sys

if len(sys.argv) == 1:
    print("Please provide a parameter.")
elif len(sys.argv) == 2:
    answer = input("What was the parameter? ")
    if answer == sys.argv[1]:
        print("Good job!")
    else:
        print("Nope sorry")
else:
    print("None")