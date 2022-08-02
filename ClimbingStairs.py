https://leetcode.com/problems/climbing-stairs/
  

class Solution:
    def climbStairs(self, n: int) -> int:
        one,two =1,1
        for i in range(n-1): #Basically this loop will run 5 times assuming i starts from 0
            temp = one
            one = one + two
            two = temp
        return one
