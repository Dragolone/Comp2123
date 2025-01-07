class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:  # 如果字符串为空，直接返回0
            return 0

        char_index = {}  # 哈希表存储字符的最后出现位置
        max_length = 0
        start = 0  # 滑动窗口的起始位置

        for end in range(len(s)):
            current_char = s[end]

            # 如果当前字符在窗口内重复，则更新窗口的起点
            if current_char in char_index and char_index[current_char] >= start:
                start = char_index[current_char] + 1

            # 更新字符的最新位置
            char_index[current_char] = end

            # 更新最大长度
            max_length = max(max_length, end - start + 1)

        return max_length
