import random

rew = [5,3,6,8,2,4,5,8,12,54,76,23,65,1,0,54,1,5,3,66,7,12]

def quick_sort(lst):
    if len(lst) < 2:
        return lst
    prop = random.randint(0,(len(lst)-1))
    leaf = []
    more = []
    for i in range(len(lst)):
        if i == prop:
            continue
        if lst[i] > lst[prop]:
            more.append(lst[i])
        else:
            leaf.append(lst[i])
    return quick_sort(leaf) + [lst[prop]] + quick_sort(more)

a = quick_sort(rew)
print(a,rew,len(a) == len(rew), sep='\n')

