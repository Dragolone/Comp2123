def kadanes_algorithm(arr):
    current_value = float('-inf')
    current_max_value = float('-inf')
    for num in arr:
        current_value = max(num, current_value + num)
        current_max_value = max(current_max_value, current_value)
    return current_max_value

arr1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(kadanes_algorithm(arr1))

