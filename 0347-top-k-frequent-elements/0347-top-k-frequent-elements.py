class Solution(object):
    def topKFrequent(self, nums, k):
        dic = {}
        for i in nums:
            if i in dic.keys():
                dic[i] += 1
            else:
                dic[i] = 1
        
        ls = list(sorted(dic.values(), reverse=True))
        res = ls[:k]
        
        r = []
        for chave,valor in dic.items():
            if valor in res:
                r.append(chave)
        return r
        