def searchRange_2(nums, target):
    # 二分法解法:左边右边分开找
    left_border = -1
    right_border = -1
    
    l, r = 0, len(nums)-1
    if r == -1:
        return [-1,-1]
    
    # 找左边
    while l < r:
        mid = l + (r - l) // 2
        if target > nums[mid]:
            l = mid + 1
        elif target < nums[mid]:
            r = mid - 1
        else:
            left_border = mid
            r = mid - 1
    
    # 找右边
    l, r = 0, len(nums)-1
    while l < r:
        mid = l + (r - l) // 2
        if target > nums[mid]:
            l = mid + 1
        elif target < nums[mid]:
            r = mid - 1
        else:
            right_border = mid
            l = mid + 1

    return [left_border, right_border]


searchRange_2([1,2,2,2,3], 2)