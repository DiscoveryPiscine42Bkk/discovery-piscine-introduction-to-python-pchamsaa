def greetings(name="noble stranger"):
    if isinstance(name, str):
        print(f"Hello, {name}!")
    else:
        print("Error: invalid name.")

greetings()
greetings("Alice")
greetings(123)