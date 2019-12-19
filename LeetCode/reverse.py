class Solution:
    def reverse(self, x: int) -> int:        
        negative = False
        
        if x < 0:
            negative = True
            x = int(str(-x)[::-1])
        else:
            x = int(str(x)[::-1])
            
        if x >= 2 ** 31- 1 or x <= -2 ** 31:
            return 0
        
        if negative:
            return -x
        else:
            return x