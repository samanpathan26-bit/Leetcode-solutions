class Solution(object):
    def validPalindrome(self, s):
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                a = s[left+1:right+1]
                b = s[left:right]
                return a == a[::-1] or b == b[::-1]

            left += 1
            right -= 1

        return True