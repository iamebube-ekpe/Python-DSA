def insertSort(uList):
    sortedResult = []
    for index in range(1, len(uList)):
        keyElement = uList[index]
        element = index - 1
        while element >= 0 and keyElement < uList[element]:
            uList[element+1] = uList[element]
            element -= 1

        uList[element+1] = keyElement
    sortedResult.append(uList)
    return sortedResult # returns a list of list -> fix

mylist = [90,2,40,1,0,20]
print(insertSort(mylist))
# print(mylist)