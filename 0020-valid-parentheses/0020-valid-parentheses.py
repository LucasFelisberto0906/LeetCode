class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        match = {"{": "}", "[": "]", "(": ")"}
        stack = []

        for ch in s:
            if ch in match:
                stack.append(ch)
            else:
                if not stack or match[stack.pop()] != ch:
                    return False
        return not stack      