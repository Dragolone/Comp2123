def merge_sort(arr):
    """
    Merge sort algorithm
    Sorts the array in ascending order
    Divide: Find hte midpoint of the array and divide it into two sub-arrays
    Conquer: Recursively sort the sub-arrays created in previous steps
    Combine: Merge the sorted sub-arrays created in previous steps
    :param arr:
    :return:
    """
    if len(arr) <= 1:
        return arr

    left_half, right_half = split(arr)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    return merge(left, right) #After reaching the bottom level, the function will return,
                              # then merge step by step upwards.

def split(arr):
    """
    Divide the unsorted array into two sub-arrays
    :param arr:
    :return: left_half, right_half
    """
    left_half = arr[:len(arr) // 2]
    right_half = arr[len(arr) // 2:]
    return left_half, right_half

def merge(left, right):
    """
    Merge sort algorithm
    :param left:
    :param right:
    :return: Returns a new merged array
    """
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # while i < len(left):
    #     l.append(left[i])
    #     i += 1
    #
    # while j < len(right):
    #     l.append(right[j])
    #     j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


alist = [54, 62, 93, 17, 77, 31, 44, 55, 20]
l1 = merge_sort(alist)
print(l1)

"""test merge_sort function"""
assert merge_sort([0]) == [0]
assert merge_sort([]) == [] #Edged case
assert merge_sort([1, 1, 9, 0 ,4 ,4, 5, 6, 1]) == [0, 1, 1, 1, 4, 4, 5, 6, 9]
assert merge_sort(alist) == [17, 20, 31, 44, 54, 55, 62, 77, 93]
assert merge_sort([1, 0, 4, 3, 2]) == [0, 1, 2, 3, 4], "Wrong result"