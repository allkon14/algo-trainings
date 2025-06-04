"""
Аня и Боря любят играть в разноцветные кубики,
причем у каждого из них свой набор и в каждом наборе все кубики
различны по цвету. Однажды дети заинтересовались, сколько существуют
цветов таких, что кубики каждого цвета присутствуют в обоих наборах.
Для этого они занумеровали все цвета случайными числами.
На этом их энтузиазм иссяк, поэтому вам предлагается помочь им в
оставшейся части. Номер любого цвета — это целое число в пределах от 0 до 10^9.

"""

n, m = map(int, input().split())
n_colors = set(int(input()) for _ in range(n))
m_colors = set(int(input()) for _ in range(m))

intersection = n_colors & m_colors
enique_n = n_colors - intersection
enique_m = m_colors - intersection

print(len(intersection))
print(*sorted(list(intersection)))
print(len(enique_n))
print(*sorted(list(enique_n)))
print(len(enique_m))
print(*sorted(list(enique_m)))
