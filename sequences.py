#string
name = "Khushnood Qadir"
print(name[0])

#lists
names = ["Khushnood","Prajjaval","Ganti"]
print(names)
print(names[0])
names.append("Marieke")
names.sort()
print(names)

#tuple
coord = (10.0, 20.0)
print(coord)
print(coord[0])


#set -> unordered
set = set()
set.add(1)
set.add(2)
set.add(3)
set.add(4)
print(set)
print(f"Set has {len(set)} elements") #len is universal.... like a global static function


#Dictionaries
os = {"Khushnood":"OpenSuse", "Prajjaval":"Windows"}
print(os["Khushnood"])
# Add another val in dict
os["Ganti"] = "OpenSuse"
print(os["Ganti"])
