# Runtime: 128 ms, faster than 96.69% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
# Memory Usage: 15 MB, less than 40.74% of Python3 online submissions for Two Sum II - Input Array Is Sorted.

numbers = [2,7,11,15]
target = 9

def twoSum(numbers: list, target: int) -> list:
    dict = {}
    for i,v in enumerate(numbers):
        if v in dict:
            return [dict[v] + 1, i + 1]
        save_num = target - v
        dict[save_num] = i

res = twoSum(numbers, target)
print(res)