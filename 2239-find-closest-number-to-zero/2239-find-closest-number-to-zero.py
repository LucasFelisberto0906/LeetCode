class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        distancias = {}
        for num in nums:
            distancias[num] = abs(num)
        
        ordenado = dict(sorted(distancias.items(), key=lambda item: (item[1], -item[0])))
        return list(ordenado.keys())[0]