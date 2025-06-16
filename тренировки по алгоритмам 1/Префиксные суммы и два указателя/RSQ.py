def count_prefixsum(nums):
    prefixsum = {0: 1}
    temp_sum = 0
    for num in nums:
        temp_sum += num
        if temp_sum in prefixsum:
            prefixsum[temp_sum] += 1
        else:
            prefixsum[temp_sum] = 0
    return prefixsum

def count_ranges_with_zero_sum(prefixsum):
    cnt = 0
    for key in prefixsum:
        cntsum = prefixsum[key]
        # Посчет количества пар
        cnt += cntsum * (cntsum - 1) // 2
    return cnt


nums = [5, -2, -3, 3, 2, -5]
prefix = count_prefixsum(nums)
print(prefix)
print(count_ranges_with_zero_sum(prefix))
