# def checkNums(nums: list, target: int) -> list:
#     length = len(nums)
#     i = 0
#     result = []
#     for i in range(length - 1):
#         j = i + 1
#         while j < length:
#             if nums[i] + nums[j] == target:
#                 result.append(i)
#                 result.append(j)
#                 return result
#             else:
#                 j += 1
#                 continue
#     return result
# List1 = [1, 3, 2, 3, 3]
# target = 6
# print(checkNums(List1, target))

class Solution(object):
    def twoSum(self, nums, target):
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i