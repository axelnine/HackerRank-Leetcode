class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict_par = {']':'[',')':'(','}':'{'}
        
        for char in s:
            if char in dict_par.values():
                stack.append(char)
            elif char in dict_par.keys:
                if stack == [] or dict_par[char] != stack.pop():
                    return False
            else:
                return True
