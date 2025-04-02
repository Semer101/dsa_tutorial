class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x >= 0:
            word = str(x)
            reverse = word[::-1]
            if word == reverse:
                return True
            else:
                return False
