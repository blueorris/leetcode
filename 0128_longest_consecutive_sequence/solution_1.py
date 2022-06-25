# Time Limit Exceeded

# nums = [100,4,200,1,3,2]
# nums = [0,3,7,2,5,8,4,6,0,1]
# nums = [1,2,0,1]
nums = [9,1,4,7,3,-1,0,5,8,-1,6]

def longestConsecutive(nums) -> int:
    nums.sort()
    print(nums)
    seq = []
    count = 0
    for i in nums:
        if seq == []:
            seq.append(i)
        else:
            if i - 1 in seq:
                seq.append(i)
            elif i == seq[0]:
                seq = [seq[-1]]
            else:
                seq = [i]
        seq = list(set(seq))
        count = max(count, len(seq))
        print(seq)
    return count

count = longestConsecutive(nums)
print(count)