class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        left, right = 0, 0

        while left != len(temperatures) - 1:
            if right == len(temperatures) - 1:
                if temperatures[right] > temperatures[left]: 
                    result.append(right - left)
                else: 
                    result.append(0)
                left += 1
                right = left 
                
            if temperatures[right] > temperatures[left]: 
                result.append(right - left)
                left += 1
                right = left 
            else:
                right += 1
        
        return result + [0]