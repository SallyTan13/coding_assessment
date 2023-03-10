import functools

def my_compare(x,y):
    if x.endswith("L"):
        if y.endswith("L"):
            if len(x) > len(y):
                return 1
            elif len(x) == len(y):
                return 0
            else:return -1
        else:
            return 1
        
    if x.endswith("M"):
        if y.endswith("L"):
            return -1
        elif y.endswith("M"):
            return 0
        else: return 1
    
    if x.endswith("S"):
        if not y.endswith("S"):
            return -1
        else:
            if len(x) > len(y):
                return -1
            elif len(x) == len(y):
                return 0
            else: return 1


N = int(input())
new_items = input().split(" ")
M = int(input())
new_reqs = input().split(" ")

new_items.sort(key=functools.cmp_to_key(mycmp=my_compare))
new_reqs.sort(key=functools.cmp_to_key(mycmp=my_compare))

idx = 0
req_id = 0
mathced_num = 0
while idx < N:
    if my_compare(new_items[idx],new_reqs[req_id]) >= 0:
        mathced_num += 1
        idx +=1
        req_id += 1
    else:
        idx += 1

# print(mathced_num)
if mathced_num == M:
    print("Yes")
else:
    print("No")