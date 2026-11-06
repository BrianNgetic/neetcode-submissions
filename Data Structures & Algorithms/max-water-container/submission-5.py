class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0;
        right = len(heights) -1;
        globalMax = 0;

        while left < right:
            height = min(heights[left], heights[right]);
            width = right - left;
            localmax = height * width;
            globalMax = max(globalMax, localmax)

            if(heights[left] < heights[right]):
                left += 1
            else:
                right -=1
            
        
         
        return globalMax;

