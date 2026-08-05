class Solution(object):
    def isPalindrome(self, s):
       temp=""
       for ch in  s:
         if ch.isalnum():
            temp+=ch.lower()
       return temp==temp[::-1]