def shell_sort(uList, uListLen):
    # eIndex = element index

    gap = uListLen // 2
    while gap > 0:
        for index in range(gap,uListLen):
            keyElement = uList[index]
            eIndex = index
            while eIndex >= gap and uList[eIndex - gap] > keyElement:
                uList[eIndex] = uList[eIndex - gap]
                eIndex -= gap

            uList[eIndex] = keyElement
        gap //= 2

myList = [90,2,20,11,0,2,4,56]
shell_sort(myList, len(myList))
print(myList)
