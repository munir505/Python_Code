from random import randint

name_list=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]

group1 = []
group2 = []
group3 = []
group4 = []


def make_group():
    while len(name_list) > 0:
        var = randint(0, len(name_list))
        group1.append(name_list[var])
        name_list.remove(name_list[var])

        var2 = randint(0, len(name_list))
        group2.append(name_list[var2])
        name_list.remove(name_list[var2])

        var3 = randint(0, len(name_list))
        group3.append(name_list[var3])
        name_list.remove(name_list[var3])

        var4 = randint(0, len(name_list))
        group4.append(name_list[var4])
        name_list.remove(name_list[var4])


make_group()

print(group1)
print(group2)
print(group3)
print(group4)