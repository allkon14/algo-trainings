a, b, c, d, e, f = map(float, [input() for _ in range(6)])

det = a * d - b * c
det_x = e * d - b * f
det_y = a * f - c * e

if det != 0 and det_x == det_y == 0:
    print(0)
elif det == det_x == det_y == 0:

    if a == b == c == d == 0:
        print(5)

    elif a == c == 0:
        if b > d:
            print(4, f"{(e - f) / (b - d):.5f}")
        else:
            print(4, f"{(f - e) / (d - b):.5f}")
    elif b == d == 0:
        if b > d:
            print(3, f"{(e - f) / (a - c):.5f}")
        else:
            print(3, f"{(f - e) / (c - a):.5f}")
    elif a > c and b > d:
        print(1, f"{(c - a) / (b - d):.5f}", f"{(e - f) / (b - d):.5f}")
    else:
        print(1, f"{(a - c) / (d - b):.5f}", f"{(f - e) / (d - b):.5f}")
elif det != 0:
    x = det_x / det
    y = det_y / det
    print(2, f"{x:.5f}", f"{y:.5f}")
