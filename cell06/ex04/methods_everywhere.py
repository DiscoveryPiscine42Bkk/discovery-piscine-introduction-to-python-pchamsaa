def shrink(s):
    return s[:8]

def enlarge(s):
    return s + 'Z' * (8 - len(s))

words = ["hi", "helloWorld", "Python", "AI"]

for word in words:
    if len(word) < 8:
        print(enlarge(word))
    else:
        print(shrink(word))
