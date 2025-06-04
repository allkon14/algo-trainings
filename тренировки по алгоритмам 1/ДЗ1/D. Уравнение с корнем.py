a, b, c = map(int, [input() for _ in range(3)])

if a == 0:
    print('MANY SOLUTIONS')
elif c < 0:
    print('NO SOLUTION')
else:
    print(int((c**2 - b) / a))