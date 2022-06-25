# Runtime: 731 ms, faster than 92.18% of Python3 online submissions for 3Sum.
# Memory Usage: 18.1 MB, less than 71.97% of Python3 online submissions for 3Sum.

nums = [-1,0,1,2,-1,-4]

def threeSum(nums):
    res = []
    nums.sort()
    
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue
        
        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = a + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return res

res = threeSum(nums)
print(res)