def make_prefix(nums):
    n = len(nums)
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + nums[i - 1]
    return prefix

n, k = map(int, input().split())
nums = list(map(int, input().split()))
prefix = make_prefix(nums)

min_sum, min_i = 9_000_000_000_000, 0
for i in range(n - k + 1):
    t_sum = prefix[i + k] - prefix[i]
    if t_sum < min_sum:
        min_sum = t_sum
        min_i = i
    # print(i, i + k, nums[i:i + k], t_sum)
print(min_i + 1)