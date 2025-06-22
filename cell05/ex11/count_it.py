import sys

if len(sys.argv) == 1:
    print("none")
else:
    print("parameter:", len(sys.argv) - 1)
    i = 1
    while i < len(sys.argv):
        print(sys.argv[i])
        i += 1