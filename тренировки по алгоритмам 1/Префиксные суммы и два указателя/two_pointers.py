def merge(nums1, nums2):
    ans = [0] * (len(nums1) + len(nums2))
    first1, first2 = 0, 0

    for k in range(len(nums1) + len(nums2)):
        if first1 != len(nums1) and (first2 == len(nums2) or nums1[first1] <= nums2[first2]):
            ans[k] = nums1[first1]
            first1 += 1
        else:
            ans[k] = nums2[first2]
            first2 += 1

    return ans


nums1 = [1, 2, 5, 7]
nums2 = [3, 4, 4]
print(merge(nums1, nums2))
