a1, b1, a2, b2 = map(int, input().split())
s = a1 * b1 + a2 * b2
sq = []

aa1 = max(a1, b1) + max(a2, b2)
bb1 = max(min(a1, b1), min(a2, b2))
if aa1 * bb1 >= s:
    sq.append((aa1, bb1))

aa2 = max(max(a1, b1), max(a2, b2))
bb2 = min(a1, b1) + min(a2, b2)
if aa2 * bb2 >= s:
    sq.append((aa2, bb2))

aa4 = max(min(a1, b1), min(a2, b2))
bb4 = max(a1, b1) + min(a2, b2)
if aa4 * bb4 >= s:
    sq.append((aa4, bb4))

print(*min(sq, key=lambda x: x[0] * x[1]))
