n, k, m = map(int, input().split())
c_zag, c_det = 0, 0

while n >= k:
    c_zag = n // k
    c_det += c_zag * (k // m)
    n -= c_zag * k

    if n % k >= m:
        c_det += 1
        n -= m
    n += c_zag * (k % m)

print(c_det)
