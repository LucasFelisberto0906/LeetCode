class Solution(object):
    def containsDuplicate(self, nums):
        verificados = set()
        for num in nums:
            if num in verificados:
                return True
            verificados.add(num)
        return False
        