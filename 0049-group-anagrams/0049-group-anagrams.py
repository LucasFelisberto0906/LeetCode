class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = {}
        for p in strs:
            words = ''.join(sorted(p))
            if words in final:
                final[words].append(p)
            else:
                final[words] = [p]
        return list(final.values())