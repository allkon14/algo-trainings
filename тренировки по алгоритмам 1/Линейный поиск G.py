nums = list(map(int, input().split()))
min_1, min_2, max_1, max_2 = 0, 0, 0, 0
for i in range(len(nums)):
    if nums[i] > max_2 and nums[i] <= max_1:
        max_2 = nums[i]
    if nums[i] > max_1:
        max_2 = max_1
        max_1 = nums[i]


    if nums[i] < min_2 and nums[i] >= min_1:
        min_2 = nums[i]

    if nums[i] < min_1:
        min_2 = min_1
        min_1 = nums[i]


print(f"{max_2} {max_1}" if max_1*max_2 > min_1*min_2 else f"{min_1} {min_2}")
