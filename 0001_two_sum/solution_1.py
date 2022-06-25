def find_num(list, target):
    dict = {}
    for i,v in enumerate(list):
        if v in dict:
            return [dict[v], i]
        save_num = target - v
        dict[save_num] = i

list = [2,7,11,15]
target = 9
res = find_num(list, target)
print(res)