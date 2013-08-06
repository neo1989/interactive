#coding:utf-8

def sequentialSearch(unorderedlist,item):
    pos = 0
    found = False
    
    while pos < len(unorderedlist) and not found:
        if unorderedlist[pos] == item:
            found = True
        else:
            pos += 1

    return found

def orderedSequentialSearch(orderedlist,item):
    pos = 0
    found = False
    stop = False

    while pos < len(orderedlist) and not found and not stop:
        if orderedlist[pos] == item:
            found = True
        elif orderedlist[pos] > item:
                stop = True
        else:
            pos +=  1 

    return found

def binarySearch(orderedlist,item):
    if len(orderedlist) == 0:
        return False
    else:
        mid = len(orderedlist)//2
        if orderedlist[mid] == item:
            return True
        elif item < orderedlist[mid]:
            return binarySearch(orderedlist[:mid],item)
        else:
            return binarySearch(orderedlist[mid+1:],item)
