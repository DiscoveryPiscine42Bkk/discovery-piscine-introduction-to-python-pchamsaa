import sys

if len(sys.argv) != 3:
    print("none")
else:
    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
        for i in range(start, end):
            print(i)
    except ValueError:
        print("none")