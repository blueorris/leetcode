nums = [100,4,200,1,3,2]
nums = [0,3,7,2,5,8,4,6,0,1]
nums = [1,2,0,1]
nums = [9,1,4,7,3,-1,0,5,8,-1,6]

def longestConsecutive(nums) -> int:
    numSet = set(nums)
    longest = 0
    
    for n in nums:
        # check if its the start of a sequence
        if (n - 1) not in numSet:
            length = 1
            while (n + length) in numSet:
                length += 1
            longest = max(length, longest)
    return longest

count = longestConsecutive(nums)
print(count)