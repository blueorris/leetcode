import collections

strs = ["eat","tea","tan","ate","nat","bat"]
def func(strs):
    ans = collections.defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            # print(c, ord(c) - ord('a'))
            count[ord(c) - ord('a')] += 1
        ans[tuple(count)].append(s)
        print(ans)
    return ans.values()

print(func(strs))