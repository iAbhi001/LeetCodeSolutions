import math

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        
        negative = (dividend < 0) ^ (divisor < 0)
        
        a, b = abs(dividend), abs(divisor)
        
        if a == 0: return 0
        if b == 1: # Optimization: skip log/exp for divisor 1 to avoid precision issues
            res = a
        else:
            # Use a slightly more aggressive epsilon or round()
            # for better precision on large dividends
            res = math.exp(math.log(a) - math.log(b))
            res = int(round(res, 10)) 

        if negative:
            res = -res
            
        return max(MIN_INT, min(MAX_INT, res))