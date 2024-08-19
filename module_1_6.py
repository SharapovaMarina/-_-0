my_dict = {"Marina": 1984, "Pavel":1983}
print("Dict:", my_dict)
print("Existing value:", my_dict["Marina"])
print("Not existing value:", my_dict.get("Nastya"))
my_dict.update({"Max": 1990, "Olga": 2001})
print("Modified dictionary:", my_dict)
my_dict.pop("Olga")
print(my_dict)

my_set = {1, 2, 3, 1, 2, "String", "String", False}
print("Set:", my_set)
my_set.add("home")
my_set.add("room")
print(my_set)
my_set.discard(2)
print(my_set)