https://leetcode.com/problems/maximum-subarray/
  
  class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0 
        maxValue = nums[0]
        for i in nums:
            if currSum < 0:
                currSum = 0 # We are discarding the sum if it is  negative and resetting the currSum to 0
            currSum +=i # Adding the number to the current sum
            maxValue = max(currSum,maxValue) # Calculating the maxValue at each step
        return maxValue
       
      
