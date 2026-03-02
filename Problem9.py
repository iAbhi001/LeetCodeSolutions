class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_s = str(x)
        if x_s ==x_s[::-1]:
            return True
        return False
        