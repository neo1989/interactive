#coding:utf-8

def sequentialSearch(alist,item):
    pos = 0
    found = False
    
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += 1

    return found

def orderedSequentialSearch(alist,item):
    pos = 0
    found = False
    stop = False

    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        elif alist[pos] > item:
                stop = True
        else:
            pos +=  1 

    return found
