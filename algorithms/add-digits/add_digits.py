class Solution:
    def addDigits(self, num: int) -> int:
        if num<9:
            return num
        else:
            return 1+(num-1)%9
        
