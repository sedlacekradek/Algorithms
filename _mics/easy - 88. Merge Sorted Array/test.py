# nums1 = [4, 3, 3, 0, 0, 0]
# nums2 = [1, 2, 6]

nums1 = [0]
m = 0
nums2 = [1]
n = 1

def merge(nums1, m, nums2, n):
    i1 = m - 1
    i2 = n - 1
    result_index = m + n - 1

    while i1 >= 0 and i2 >= 0:
        if nums1[i1] > nums2[i2]:
            nums1[result_index] = nums1[i1]
            i1 -= 1
        else:
            nums1[result_index] = nums2[i2]
            i2 -= 1
        result_index -= 1
    if i2 >= 0:
        nums1[:result_index+1] = nums2[:i2+1]
    return nums1




print(merge(nums1=nums1, m=m, nums2=nums2, n=n))
print(nums1)