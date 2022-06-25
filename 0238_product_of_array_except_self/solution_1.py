# Time Limit Exceeded

import numpy as np
def productExceptSelf(nums):
    res_list = []
    for i in nums:
        left_list = [i for i in nums]
        left_list.remove(i)
        left_arr = np.array(left_list)
        prod = np.prod(left_arr)
        # print(raw_list)
        res_list.append(prod)
    return res_list

nums = [1,2,3,4]
res = productExceptSelf(nums)
print(res)