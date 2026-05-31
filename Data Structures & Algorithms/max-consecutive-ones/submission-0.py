class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_one = 0
        count = 0

        for num in nums:
            if num:
                count += 1
            else:
                max_one = count if count > max_one else max_one
                count = 0

        max_one = count if count > max_one else max_one
        return max_one