"""
Геном жителей системы Тау Кита содержит 26 видов оснований, для обозначения которых будем использовать буквы латинского алфавита от A до Z, а сам геном записывается строкой из латинских букв. Важную роль в геноме играют пары соседних оснований, например, в геноме «ABBACAB» можно выделить следующие пары оснований: AB, BB, BA, AC, CA, AB.

Степенью близости одного генома другому геному называется количество пар соседних оснований первого генома, которые встречаются во втором геноме.
"""


def add_to_set(genom):
    genom_set = set()
    for i in range(len(genom) - 1):
        genom_set.add(genom[i:i + 2])
    return genom_set


def add_to_dict(genom):
    genom_dict = {}
    for i in range(len(genom) - 1):
        if genom[i:i + 2] in genom_dict:
            genom_dict[genom[i:i + 2]] += 1
        else:
            genom_dict[genom[i:i + 2]] = 1
    return genom_dict


first = input()
second = input()
first_dict = add_to_dict(first)
second_set = add_to_set(second)

ans = 0
for gen in second_set:
    ans += first_dict.get(gen, 0)
print(ans)
