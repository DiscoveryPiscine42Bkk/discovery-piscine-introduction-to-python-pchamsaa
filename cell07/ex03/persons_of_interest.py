def famous_births(birth_dict):
    sorted_births = sorted(birth_dict.values(), key=lambda x: x["date_of_birth"])
    for person in sorted_births:
        print(f"{person['name']} was born in {person['date_of_birth']}")

if __name__ == "__main__":
    persons = {
        "einstein": {"name": "Albert Einstein", "date_of_birth": 1879},
        "curie": {"name": "Marie Curie", "date_of_birth": 1867},
        "turing": {"name": "Alan Turing", "date_of_birth": 1912},
        "lovelace": {"name": "Ada Lovelace", "date_of_birth": 1815},
        "newton": {"name": "Isaac Newton", "date_of_birth": 1643}
    }
    famous_births(persons)
