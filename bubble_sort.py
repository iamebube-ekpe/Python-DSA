def bubbleSort(uList):
    sizeOfList = len(uList) - 1

    for num in range(sizeOfList):
        for index in range(sizeOfList-num):
            if uList[index] > uList[index+1]:
                uList[index],uList[index+1] = uList[index+1], uList[index]

    return uList

userList = input("Enter a list of values (seperated with spaces): ").replace(",", " ").split()
userList = [int(x) for x in userList]
print(f"You entered: {userList}")
print(f"Bubble Sorted List: {bubbleSort(userList)}")