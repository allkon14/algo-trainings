ss = "А. Стильная одежда B. Сумма номеров D. Город Че E. Красота превыше всего F. Кондиционеры G. Счет в гипершашках H. Подстрока J. Треугольники"
l = ss.split()

ans = []
i = 0
t = []
while i < len(l):
    if l[i].__contains__('.'):
        t.append(l[i])
        i += 1
        while i < len(l) and not l[i].__contains__('.'):
            t.append(l[i])
            i += 1
        print(t)
        ans.append(' '.join(t))
        t = []
print(ans)