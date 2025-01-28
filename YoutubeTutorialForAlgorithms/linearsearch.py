class LinearSearch:
    def linear_search(self, list, target):
        for i in range(len(list)):
            if list[i] == target:
                return f"Found at index {i}"
        return -1


print(LinearSearch().linear_search([1, 2, 3, 4, 5], 5))
print(LinearSearch().linear_search([100, 58, 34, 234, 909], 5))


