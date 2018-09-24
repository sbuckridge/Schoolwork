#Sam Buckridge
#CS 3060 13:00-14:15
#Assignment 3: Python Functions

import sys


#insertion sort function
def insertion_sort(array):
    for i in range(1, len(array)): #Start at second element to compare to the 0th element
        key = array[i]

        k = i - 1
        while k >= 0 and key < array[k]: #loop through while k is at or above 0 and the item to the right is less than the left
            array[k+1] = array[k] #shift num at k right to k+1
            k -= 1
        array[k+1] = key


#binary search function
def binary_search(array, item, offset=0):
    mid = int(len(array)/2) #make mid an int so it truncates
    if len(array) == 1 and array[0] != item: #If the array gets down to 1 item and it's not what we're looking for,
        return None                          #then return None.

    if item == array[mid]: #if the item is at mid, we're done
        return mid + offset
    elif item > array[mid]: #if the item is bigger than the item at mid, go to right side of array
        return binary_search(array[mid:], item, offset+mid) #add the mid value to offset since we're going right
    else: #otherwise, the value is smaller and we go to the left side of the array
        return binary_search(array[:mid], item, offset) #leave offset the same


def split_char(initStr, splitChar):
    newList = [] #declaring a list to add the strings into
    temp = "" #declaring a temp string to hold the letters until the splitChar is reached

    for i in range(0, len(initStr)): #walks through the initial string
        if initStr[i] != splitChar: #if the char at initStr[i] isn't the split char, add onto the temp string
           temp += initStr[i]
        else: #if the char at initStr[i] is the split char, append temp string and move to next letter
            newList.append(temp)
            temp = "" #clear the temp string

    newList.append(temp) #I honestly don't really know why this line makes the function work,
    print(newList)       #but it does, so I won't complain.
