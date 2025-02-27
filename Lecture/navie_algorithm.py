def naive_max_subarray_sum(arr):
    if not arr:
        return float('-inf')

    n = len(arr)
    max_sum = float('-inf')
    for i in range(n):
        for j in range(i, n):
            # Calculate the sum from all the sublist.
            current_sum = 0
            for k in range(i, j + 1):
                current_sum += arr[k]
            max_sum = max(max_sum, current_sum)

    return max_sum

arr1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(naive_max_subarray_sum(arr1))