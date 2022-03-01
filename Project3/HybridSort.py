"""
Name: Justin Vesche
PID: A56742340
"""


def quick_sort(unsorted, threshold, start, end, reverse=False):
    """
    A hybrid sort that that depending on the threshold
    can convert from quicksort to insertion sort
    """
    length = end - start + 1
    if length <= threshold:
        insertion_sort(unsorted, start, end, reverse)
        return
    elif start >= end:
        return

    piv = subdivide(unsorted, start, end, reverse)
    quick_sort(unsorted, threshold, start, piv - 1, reverse)
    quick_sort(unsorted, threshold, piv + 1, end, reverse)

    pass


def subdivide(unsorted, start, end, reverse):
    """
    Look through the list from start to end of the, and place
    items before and after the pivot. Return the index of the pivot.
    """
    midpoint = find_pivot(unsorted, start, end)
    index = None
    if unsorted[end] == midpoint:
        index = end
    elif unsorted[((end - start) // 2) + start] == midpoint:
        index = ((end - start) // 2) + start
    else:
        index = start
    unsorted[index], unsorted[end] = unsorted[end], unsorted[index]
    index = end
    low = start
    high = end - 1
    while low <= high:
        if reverse:
            while low <= high and unsorted[low] > midpoint:
                low += 1
            while low <= high and midpoint > unsorted[high]:
                high -= 1
            if low <= high:
                unsorted[low], unsorted[high] = unsorted[high], unsorted[low]
                low += 1
                high -= 1
        else:
            while low <= high and unsorted[low] < midpoint:
                low += 1
            while low <= high and midpoint < unsorted[high]:
                high -= 1
            if low <= high:
                unsorted[low], unsorted[high] = unsorted[high], unsorted[low]
                low += 1
                high -= 1
    if reverse:
        index = low
        unsorted[index], unsorted[end] = unsorted[end], unsorted[index]
    else:
        index = low
        unsorted[index], unsorted[end] = unsorted[end], unsorted[index]
    return index


def find_pivot(unsorted, start, end):
    """
    Use median of three to find the correct pivot.
    Once found, return the amount of pivot.
    """
    midpoint = ((end - start) // 2) + start
    if end - start <= 1:
        return unsorted[end]
    elif ((unsorted[start] < unsorted[midpoint] < unsorted[end]) or
          (unsorted[end] < unsorted[midpoint] < unsorted[start])):
        return unsorted[midpoint]
    elif ((unsorted[midpoint] < unsorted[start] < unsorted[end]) or
          (unsorted[end] < unsorted[start] < unsorted[midpoint])):
        return unsorted[start]
    elif ((unsorted[midpoint] < unsorted[end] < unsorted[start]) or
          (unsorted[start] < unsorted[end] < unsorted[midpoint])):
        return unsorted[end]
    elif unsorted[start] == unsorted[midpoint] and unsorted[midpoint] < unsorted[end]:
        return unsorted[midpoint]
    else:
        return unsorted[end]


def insertion_sort(unsorted, start, end, reverse):
    """
    Use insertion to properly sort the list. Look upon
    if the list should be reversed or not.
    """
    length = end - start
    for i in range(start + 1, start + length + 1):
        j = i
        if reverse:
            while j > start and unsorted[j] > unsorted[j - 1]:
                unsorted[j], unsorted[j - 1] = unsorted[j - 1], unsorted[j]
                j -= 1
        else:
            while j > start and unsorted[j] < unsorted[j - 1]:
                unsorted[j], unsorted[j - 1] = unsorted[j - 1], unsorted[j]
                j -= 1


def largest_sequential_difference(lst):
    """
    Use quick_sort to first sort the list, if there is less than 2 items
    in list return none. The sort uses insertion if there is a threshold of
    6. Then linearly look through the list, keeping O(nlogn) time.
    """
    size = len(lst)
    if size < 2:
        return None
    quick_sort(lst, 6, 0, size - 1, False)
    largest_difference = 0
    for i in range(size - 1):
        if lst[i + 1] - lst[i] > largest_difference:
            largest_difference = lst[i + 1] - lst[i]
    return largest_difference
