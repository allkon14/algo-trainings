n = int(input())
nl = list(map(int, input().split()))
m = int(input())
ml = list(map(int, input().split()))

f1, f2 = 0, 0
best_i, best_j = -1, -1
min_dif = 100000000
t = 0
while f1 != n and f2 != m:
    if nl[f1] == ml[f2]:
        best_i, best_j = f1, f2
        break

    if abs(ml[f2] - nl[f1]) <= min_dif:
        min_dif = abs(ml[f2] - nl[f1])
        best_i, best_j = f1, f2

    if nl[f1] < ml[f2]:
        f1 += 1
    else:
        f2 += 1
    # print(f'{f1:<5} {nl[f1]:<5} {f2:<5} {ml[f2]:<5} {ml[f2] - nl[f1]:<5} {min_dif:<5}')

print(nl[best_i], ml[best_j])
