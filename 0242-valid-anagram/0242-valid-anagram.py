class Solution(object):
    def isAnagram(self, s, t):
        l1 = sorted(list(s))
        l2 = sorted(list(t))
        return l1 == l2