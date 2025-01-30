class BinarySearch:
    @staticmethod
    def binary_search(array, target):
        first = 0
        last = len(array) - 1
        while first <= last:
            midpoint = (first + last) // 2
            if array[midpoint] == target:
                return midpoint
            elif array[midpoint] < target:
                first = midpoint + 1
            else:
                last = midpoint - 1
        return -1

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
test_cases = {
    3: 2,
    8: 7,
    9: 8,
    100: -1,
    15: 14
}

for target, expected_index in test_cases.items():
    result = BinarySearch.binary_search(array, target)
    assert result == expected_index, f"Test failed for target {target}: expected {expected_index}, got {result}"

print("All tests passed!")