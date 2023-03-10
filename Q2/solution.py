num = int(input())
allValid = True
errorCodes = []
for i in range(num):
    item_list = input().split()
    if item_list[1] == 'false':
        allValid = False
        errorCodes.append(item_list[2])

if allValid:
    print("Yes")
else:
    print("No")
    for i in range(len(errorCodes)):
        if i == len(errorCodes) - 1:
            print(errorCodes[i], end="")
        else:
            print(errorCodes[i], end=" ")

