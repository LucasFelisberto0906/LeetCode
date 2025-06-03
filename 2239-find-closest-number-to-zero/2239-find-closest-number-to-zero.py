class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        distancias = {}
        for num in nums:
            distancia = abs(num)
            distancias[num] = distancia
        
        ordenado = dict(sorted(distancias.items(), key=lambda item: (item[1], -item[0])))
        return list(ordenado.keys())[0]