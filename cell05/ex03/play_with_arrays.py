original = [2, 5, 8, 8, 22, -12, 92]

filtered = [x for x in original if x > 5]
new_array = [x + 2 for x in filtered]
unique_array = []
for num in new_array:
    if num not in unique_array:
        unique_array.append(num)

print(unique_array)