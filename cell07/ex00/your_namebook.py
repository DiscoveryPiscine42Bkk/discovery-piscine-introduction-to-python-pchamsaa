def array_of_name(name_dict):
    full_names = []
    for last, first in name_dict.items():
        full_name = f"{first.capitalize()} {last.capitalize()}"
        full_names.append(full_name)
    return full_names

persons = {
    "lovelace": "ada",
    "hopper": "grace",
    "torvalds": "linus",
    "bridges": "ruby"
}
print(array_of_name(persons))