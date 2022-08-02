https://leetcode.com/problems/jump-game/
  
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        for i in range(len(nums)-1,-1,-1): #Greedy approach. Start from the right and decrement by 1 till u reach the first position
            if i+nums[i]>=goal: #Checking whether the number at index is greater than or equal to goal. If yes then shift the goal towards left 
                goal = i 
        return True if goal ==0 else False
      
      
