class BinarySearch:
    @staticmethod
    def binary_search(array, target):
        first = 0
        last = len(array) - 1
        while first <= last:
            midpoint = (first + last) // 2  # 5 -> 2  8 -> 4
            if array[midpoint] == target:
                return f"Target is found on index {midpoint}"
            elif array[midpoint] < target:
                first = midpoint + 1
            else:
                last = midpoint - 1
        return -1

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
target_list = [3, 8, 9, 100, 15]
for target in target_list:
    index = BinarySearch.binary_search(array, target)
    if index != -1:
        print(f"{target} found at index {index}")
    else:
        print(f"{target} not found")