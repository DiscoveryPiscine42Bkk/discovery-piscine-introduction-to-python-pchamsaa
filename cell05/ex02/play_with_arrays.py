original = [2, 5, 8, 8, 22, -12, 92]
filtered = [x for x in original if x > 5]
new_array = [x + 2 for x in filtered]

print(filtered)
print(new_array)