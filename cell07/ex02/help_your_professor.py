def average(scores_dict):
    total = sum(scores_dict.values())
    count = len(scores_dict)
    return total / count

class_a = {
    "John": 88,
    "Jane": 92,
    "Tom": 75,
    "Lucy": 80
}

class_b = {
    "Anna": 95,
    "Mike": 78,
    "Leo": 85
}

print(f"Average for class A: {average(class_a):.2f}")
print(f"Average for class B: {average(class_b):.2f}")