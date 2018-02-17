class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        
        for char in ops:
            temp = 0
            if int(char) == int and int(char) <30000 and int(char) > -30000:
                stack.append(int(char))
                length = len(stack)
            elif char == '+' and length > 1:
                temp = stack[length-1] + stack[length-2]
                stack.append(temp)
                length = len(stack)
            elif char == 'D' and length >0:
                temp = 2*stack[length-1]
                length = len(stack)
            elif char == 'C' and length>0:
                stack.pop()
                length = len(stack)
        
        print sum(stack)
