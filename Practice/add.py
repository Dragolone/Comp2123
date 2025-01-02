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
        num_map = {}  # 创建一个哈希表
        for i, num in enumerate(nums):  # 遍历数组
            complement = target - num   # 计算补数
            if complement in num_map:  # 如果补数已经存在于哈希表中
                return [num_map[complement], i]
            num_map[num] = i  # 否则，存入哈希表
