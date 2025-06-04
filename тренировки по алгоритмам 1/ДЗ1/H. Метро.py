a, b, n, m = map(int, [input() for _ in range(4)])

min_a = (a + 1) * (n - 1) + 1
max_a = min_a + 2 * a

min_b = (b + 1) * (m - 1) + 1
max_b = min_b + 2 * b

min_ans = max(min_a, min_b)
max_ans = min(max_a, max_b)

if min_ans <= max_ans:
    print(min_ans, max_ans)
else:
    print(-1)
