#coding:utf-8

def bubbleSort(alist):
    """冒泡排序"""
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

    return alist

def selectSort(alist):
    """选择排序"""
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax = 0
        for location in range(1,fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        tmp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = tmp

    return alist

def insertionSort(alist):
    """插入排序"""
    for index in range(1,len(alist)):
        currentValue =  alist[index]
        position = index

        while position > 0 and alist[position-1] > currentValue:
            alist[position] = alist[position-1]
            position = position - 1
        
        alist[position] = currentValue

    return alist
    
def shellSort(alist):
    """希尔排序"""
    pass




        
