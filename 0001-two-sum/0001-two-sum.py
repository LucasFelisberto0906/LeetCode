class Solution(object):
    def twoSum(self, nums, target):
        res = {}
        for i, num in enumerate(nums):
            valor = target - num
            if valor in res:
                return [i, res[valor]]
            res[num] = i
        return []