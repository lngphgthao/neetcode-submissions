class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
            
        start, end = 0, 1
        max_len = 0

        while end != len(s):
            if s[end] not in s[start:end]:
                end += 1
            else: 
                length = end - start
                max_len = length if length > max_len else max_len
                start += 1
                end = start + 1

        max_len = end - start if end - start > max_len else max_len
        return max_len