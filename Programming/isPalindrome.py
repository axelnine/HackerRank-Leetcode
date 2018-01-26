# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 18:17:08 2017

@author: iGuest
"""

def isPalindrome(s):
        """
        :type s: str
        :rtype: bool
        """
        flag = 0
        flag_2 = 0
        s = ''.join(x for x in s if x.isalnum())
        s = s.lower()
        string_length = len(s)
        if string_length%2 == 0:
            mid_point = int(string_length/2)
        else:
            flag_2 = 1
            mid_point = int((string_length + 1)/2)
        if flag_2 == 1:
            for i in range(0,(mid_point-1)):
                if s[i] == s[string_length-i-1]:
                    flag = flag + 1;
        else:
            for i in range(0,(mid_point)):
                if s[i] == s[string_length-i-1]:
                    flag = flag + 1;
    
        if s == '' or len(s) == 1:
            return True
        elif len(s) == 2:
            if s[0] == s[1]:
                return True
            else:
                return False
        elif flag == (mid_point-1) and flag_2 == 1:
            return True
        elif flag == mid_point:
            return True
        else:
            return False
            
print(isPalindrome('abb'))

def isPalRec(st, s, e) :
     
    # If there is only one character
    if (s == e):
        return True
 
    # If first and last characters do not match
    if (st[s] != st[e]) :
        return False
 
    # If there are more than two characters,
    # check if middle substring is also
    # palindrome or not.
    if (s < e+1) :
        return isPalRec(st, s+1, e-1);
 
    return True
 