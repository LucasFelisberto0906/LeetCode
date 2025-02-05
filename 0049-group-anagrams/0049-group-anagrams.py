class Solution(object):
    def groupAnagrams(self, strs):
        final = {}
        for p in strs:
            palavras = ''.join(sorted(p))
            if palavras in final:
                final[palavras].append(p)
            else:
                final[palavras] = [p]
                    
        return list(final.values())


            
            