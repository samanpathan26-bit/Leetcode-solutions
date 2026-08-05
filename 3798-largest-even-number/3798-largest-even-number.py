class Solution(object):
    def largestEven(self, s):
        index=-1
        for i in range(len(s)):
            if s[i]=='2':
                index=i
        if index==-1:
            return ""
        else:
            return s[:index+1]
