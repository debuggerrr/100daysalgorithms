https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res=0
        l,r = 0,len(height)-1
        while l < r:
            area = (r-l)*(min(height[l],height[r])) # Subtract rightmost pointer with the left pointer to calculate the width and multiply it with the min of heights
            res = max(area,res)
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return res
