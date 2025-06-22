import sys

if len(sys.argv) == 1:
    print("none")
else:
    i = 1
    while i < len(sys.argv):
        word = sys.argv[i]
        if not word.startswith("start"):
            print(f"parameter_ready: {word}_ready")
        i += 1
