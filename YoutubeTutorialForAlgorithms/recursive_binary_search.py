def recursive_binary_search(arr, target) -> bool:
    # By default, the arr is sorted from the lowest to the highest
    if len(arr) == 0:
        return False
    else:
        mid = len(arr) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            return recursive_binary_search(arr[mid+1:], target)
        else:
            return recursive_binary_search(arr[:mid], target)
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert recursive_binary_search(arr, 7) == True
assert recursive_binary_search(arr, 8) == False
assert recursive_binary_search(arr, 9) == False