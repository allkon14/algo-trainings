def type_1(prefix, l, r):
    return prefix[r] - prefix[l]


def type_2(prefix, l, r):
    return prefix[r] - prefix[l]


def make_prefix(nums):
    n = len(nums)
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + nums[i - 1]
    return prefix


n = int(input())
nums = list(map(int, input().split()))
sort_nums = sorted(nums)

pref_nums = make_prefix(nums)
pref_sort_nums = make_prefix(sort_nums)

m = int(input())
for _ in range(m):
    type, l, r = map(int, input().split())
    if type == 1:
        print(type_1(pref_nums, l - 1, r))
    else:
        print(type_2(pref_sort_nums, l - 1, r))
