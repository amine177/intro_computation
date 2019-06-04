#!/bin/env python


# this maybe faster because it uses the python native methods

def merge(l1, l2, predicate):
    """
    Merges tow lists according to a predicate
    Input:
        l1: a list of objects defining __lt__()
        l2: a list of objects defining __lt__()
    Output:
        a merged list according to predicate
    Example:
        merge([1, 3], [-5, 2, 4, ], lambda x, y: x < y ) -> [-5, 1, 2, 3, 4]
    """

    i, j = 0, 0
    result = []
    while i < len(l1) and j < len(l2):
        if predicate(l1[i], l2[j]):
            result.append(l1[i])
            i += 1
        else:
            result.append(l2[j])
            j += 1

    while i < len(l1):    # if len(l1) > len(l2) or len(2) > len(1)
                          # copy rest of values
        result.append(l1[i])
        i += 1
    while j < len(l2):
        result.append(l2[j])
        j += 1

    return result

def mergeSort(L, predicate = lambda x, y: x < y):

    """
    Sorts a list according to a predicate
    Input:
        L: list of objects defining __lt__()
        predicate: function that takes as parameters tow objects
                   defining __lt__()
    Output:
        a sorted list which is a result of merging tow sub sorted lists
    """


    if len(L) < 2:  # a one element list is sorted by definition
        return L[:] # forcing a cloning of L
    else:
        m = len(L) // 2
        sub_left = mergeSort(L[:m], predicate)
        sub_right = mergeSort(L[m:], predicate)
        return merge(sub_left, sub_right, predicate)

if __name__ == "__main__":
    print(mergeSort([3, -2, 101, -5, 3, 4, -1, 0]))
