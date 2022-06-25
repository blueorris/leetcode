# Time Limit Exceeded

nums = [-1,0,1,2,-1,-4]
from itertools import combinations

def threeSum(nums):
    res_list = []
    for p in combinations(nums, 3):
        if sum(p) == 0:
            sort_list = sorted(p)
            if sort_list not in res_list:
                res_list.append(sort_list)
    return res_list

res = threeSum(nums)
print(res)
