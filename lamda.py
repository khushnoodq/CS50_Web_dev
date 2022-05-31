people = [
    {"name": "Khushnood", "OS": "OpenSuse"},
    {"name": "Prajjaval", "OS": "Windows"},
    {"name": "Ganti", "OS": "OpenSuse"},
]

def sortName(person):
    return person["name"]

def sortOS(os):
    return os["OS"]

people.sort(key=sortName)
print(people)
people.sort(key=sortOS)
print(people)
people.sort(key=lambda person: person["name"])
print(people)
