class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums) - nums.count(val)

        for _ in range(nums.count(val)):
            nums.remove(val)

        return k