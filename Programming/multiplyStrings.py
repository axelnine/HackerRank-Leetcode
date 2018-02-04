class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        value = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        result_num1 = 0
        result_num2 = 0
        for digit in num1:
            result_num1 = 10 * result_num1 + value[digit]
        for digit in num2:
            result_num2 = 10 * result_num2 + value[digit]
            
        return(str(result_num1*result_num2))
        
