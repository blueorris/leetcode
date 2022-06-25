# Runtime: 142 ms, faster than 48.36% of Python3 online submissions for Top K Frequent Elements.
# Memory Usage: 18.8 MB, less than 41.52% of Python3 online submissions for Top K Frequent Elements.

from collections import defaultdict

def topKFrequent(nums, target):
    cnt_dict = defaultdict(int)
    for k in nums:
        cnt_dict[k] += 1
    # print(cnt_dict)
    sort_dict = {k: v for k, v in sorted(cnt_dict.items(), key=lambda item: item[1], reverse=True)}
    # print(sort_dict)
    res_list = []
    for key in sort_dict.keys():
        res_list.append(key)
    print(res_list)
    return res_list[:target]

nums = [1,1,1,2,2,3]
k = 2
res = topKFrequent(nums, k)
print(res)