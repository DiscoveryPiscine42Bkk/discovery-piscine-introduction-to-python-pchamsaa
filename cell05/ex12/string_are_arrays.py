import sys

if len(sys.argv) != 2:
    print("none")
else:
    string = sys.argv[1]
    i = 0
    while i < len(string):
        if string[i] == 'a':
            print(f"The character 'a' is found at index: {i}")
        i += 1