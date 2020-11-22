def select_sort(uList, uListLen):
    # feIndex = first element index

    for feIndex in range(uListLen):
        minimum = feIndex
        for index in range(feIndex + 1, uListLen):
            if uList[index] < uList[minimum]:
                minimum = index
        
        (uList[feIndex],uList[minimum]) = (uList[minimum], uList[feIndex])

myList = [34,1,23,12,2,0]
select_sort(myList, len(myList))
print(myList)