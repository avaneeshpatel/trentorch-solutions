def count_comparisons_linear_search(arr, target):
    """
    arr:    a list of numbers
    target: the value being searched for

    Returns:
        (found, comparisons): found is True if target is in arr, False
        otherwise. comparisons is the number of element-to-target
        comparisons actually performed (stop as soon as a match is
        found -- don't keep scanning).
    """
    # TODO: Implement a left-to-right linear scan, counting comparisons.
    for i in range(len(arr)):
        if arr[i] == target:
            return (True,i+1)
    return (False,len(arr))


def count_comparisons_binary_search(sorted_arr, target):
    """
    sorted_arr: a list of numbers, already sorted ascending
    target:     the value being searched for

    Returns:
        (found, comparisons): same shape as count_comparisons_linear_search,
        but using binary search -- each comparison must actually halve
        the remaining search space.
    """
    # TODO: Implement binary search from Theory, counting one
    # comparison per midpoint check.
    comparison = 0
    start = 0
    end = len(sorted_arr)-1
    while start <= end:
        mid = (start+end)//2
        comparison += 1
        if sorted_arr[mid] == target:
            return (True,comparison)
        elif sorted_arr[mid] < target:
            start = mid+1
        else:
            end = mid-1
    return (False,comparison)
