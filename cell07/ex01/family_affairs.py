def find_the_redheads(family_dict):
    return list(filter(lambda name: family_dict[name] == "red", family_dict))

doe_family = {
    "Jessica": "blonde",
    "Ashley": "red",
    "Emily": "black",
    "Thomas": "red",
    "John": "brown"
}
print(find_the_redheads(doe_family))