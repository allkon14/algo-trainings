a, b, c, d, e = map(int, [input() for _ in range(5)])
max_de = max(d, e)
min_de = min(d, e)
if (max(a, b) <= max_de and min(a, b) <= min_de) or (max(c, b) <= max_de and min(c, b) <= min_de) or (
        max(a, c) <= max_de and min(a, c) <= min_de):
    print("YES")
else:
    print("NO")


# Выбор первого и второго максимума из трех чисел (ручная сортировка пузырьком)
# сравниваем числа и меняем их порядок, если он неверный
# Пример:
# 1) 10 7 5 -> 7 10 5 -> 7 5 10 (за первый проход самый тяжелы элемент утонул)
# 2) 7 5 10 -> 5 7 10
