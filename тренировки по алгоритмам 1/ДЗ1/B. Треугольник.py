a, b, c = map(int, [input() for _ in range(3)])

print("YES" if a + b > c and a + c > b and b + c > a else "NO")
