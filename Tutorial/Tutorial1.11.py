def check_duplicate_elements1(arr) -> bool:
    """
    Time Complexity: O(n**2)
    :param arr: array of elements
    :return: Boolean
    """
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False

def check_duplicate_elements2(arr) -> bool:
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False

