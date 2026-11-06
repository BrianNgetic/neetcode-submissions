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
                height = heights[left]
                left += 1
                while heights[left] < height:
                    left += 1
            else:
                height = heights[right]
                right -=1
                while heights[right] < height:
                    right -= 1;
            
        
         
        return globalMax;

