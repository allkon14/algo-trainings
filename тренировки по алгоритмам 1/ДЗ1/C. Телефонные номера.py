new = "".join(input().split('-')).replace('(', '').replace(')', '')
code_new = "495"
num_new = "0000000"

if new[0] == '8':
    if len(new) == 11:
        code_new = new[1:4]
        num_new = new[4:]
    elif len(new) == 8:
        num_new = new[1:]

elif new[0] == '+':
    if len(new) == 12:
        code_new = new[2:5]
        num_new = new[5:]
    elif len(new) == 9:
        num_new = new[2:]

elif len(new) == 7:
    num_new = new[:]

for _ in range(3):
    code_cur = '495'
    num_cur = "0000000"

    cur = "".join(input().split('-')).replace('(', '').replace(')', '')

    if cur[0] == '8':
        if len(cur) == 11:
            code_cur = cur[1:4]
            num_cur = cur[4:]
        elif len(cur) == 8:
            num_cur = cur[1:]

    elif cur[0] == '+':
        if len(cur) == 12:
            code_cur = cur[2:5]
            num_cur = cur[5:]
        elif len(new) == 9:
            num_cur = cur[2:]

    elif len(cur) == 7:
        num_cur = cur[:]

    if code_cur == code_new and num_cur == num_new:
        print("YES")
    else:
        print("NO")
