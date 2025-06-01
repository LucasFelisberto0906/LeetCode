class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        left = 0
        right = len(numbers) - 1
        while(left < right):
            soma = numbers[left] + numbers[right]
            if(soma == target):
                return [left + 1, right + 1]
            elif(soma > target):
                right -= 1
            else:
                left += 1
        return []        
        