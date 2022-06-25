strs = ["eat","tea","tan","ate","nat","bat"]

def groupAnagrams(strs):
    sort_strs  = [''.join(sorted(i)) for i in strs]
    # print(sort_strs)
    dict = {}
    for i,v in enumerate(sort_strs):
        if v not in dict:
            dict[v] = [strs[i]]
        else:
            dict[v].append(strs[i])
    return dict.values()

res = groupAnagrams(strs)
print(res)