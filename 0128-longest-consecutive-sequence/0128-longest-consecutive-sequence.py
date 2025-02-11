class Solution(object):
    def longestConsecutive(self, nums):
        max_sequencia = 0
        ordenada = set(nums)
        for i in ordenada:
            if i-1 not in ordenada:
                comp = 1
                while i + 1 in ordenada:
                    comp +=1
                    i+=1
                max_sequencia = max(comp, max_sequencia)

        return max_sequencia
        