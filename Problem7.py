class Solution:
    def reverse(self, x: int) -> int:
        if x < 0 :
            x = -1 * x 
            x = str(x)
            x = x[::-1]
            print(x)
            x = -1 * (int(x))
            return x 
        else:
            x = str(x)
            x = x[::-1]
            print(x)
            x = int(int (x))
            return x

        