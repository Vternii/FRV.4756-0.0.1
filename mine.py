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

def binary_search(lst, val):
    max = len(lst) - 1
    min = 0
    last_mid = None
    while True:
        mid = (max + min) // 2
        if mid == last_mid:
            if mid != len(lst) - 1 and mid != 0:
                if val < 0:
                    val *= -1
                if abs(val - lst[mid]) > abs(val - lst[mid+1]):
                    mid = mid+1
            return f"val - {val} is not found, nearest val is {lst[mid]} on index {mid}"
        elif val == lst[mid]:
            return f"val - {val} on index {mid}"
        elif val > lst[mid]:
            min = mid + 1
        elif val < lst[mid]:
            max = mid - 1
        last_mid = mid
        
if __name__ == '__main__':
    print(binary_search(a,5))
    print(binary_search(a,10))
    print(binary_search(a,20))
    print(binary_search(a,40))
    print(binary_search(a,23))
    print(binary_search(a,66))
    print(binary_search(a,69))
    print(binary_search(a,74))
    print(binary_search(a,100))


