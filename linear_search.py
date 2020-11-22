def linear_search(uList, uListLen, key):
    for index in range(0, uListLen):
        if(uList[index] == key):
            return index
    return -1

myList = [2,4,3,9,6]
matched = linear_search(myList, len(myList), 9)
if (matched == -1):
    print("The inputed key is not present")
else:
    print(f"The key is present at index: {matched}")