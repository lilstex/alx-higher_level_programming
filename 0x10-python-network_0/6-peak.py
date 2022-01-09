#!/bin/bash
# Finds a peak in a list of unsorted integers.
def find_peak(list_of_integers):
    """This function finds a peak in a list of unsorted integers"""
    if list_of_integers == []:
        return None

    a = len(list_of_integers)
    if a == 1:
        return list_of_integers[0]
    if a == 2:
        return max(list_of_integers)
    
    # Find the middle element
    mid = int(a / 2)
    # Check if the middle element is greater than its neighbours
    if(list_of_integers[mid] >= list_of_integers[mid-1] and list_of_integers[mid] >= list_of_integers[mid+1]):
        return list_of_integers[mid]

    # If the left neighbor of mid is greater than the middle element,
    # find the peak recursively in the left sublist
    if(list_of_integers[mid] <= list_of_integers[mid-1]):
        return find_peak(list_of_integers[:mid])

    # If the left neighbor of mid is greater than the middle element,
    # find the peak recursively in the left sublist
    if(list_of_integers[mid] <= list_of_integers[mid+1]):
        return find_peak(list_of_integers[mid+1:])
