'''
Created on 2012-4-15

@author: Snap_Zhan

This package is used to search one key from the list, constained multiple search algrithm.
'''

def line_search(key, mylist):
    '''
    line search from the input the list
    Return Value:
    index of the key in the list
    -1: Not Found
    '''
    
    if (not key):
        print "Key is empty"
        return -1
    
    if (not mylist):
        print "list is empty"
        return -1
    
    index = 0
    found = False
    for tmpkey in mylist:
        if(tmpkey == key):
            found=True
            break
        index += 1
    
    if found:
        return index
    else:
        return -1
    
    
