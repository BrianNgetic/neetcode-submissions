class Solution:
    def maxArea(self, heights: List[int]) -> int:
        globalVolume = 0;
        left = 0;
        right = len(heights) -1;

        while left <= right :
            width = right - left
            height  = min(heights[left], heights[right])

            localVolume =  height * width
            globalVolume = max(globalVolume, localVolume)

            if heights[left] < heights[right]:
                height =  heights[left]
                left += 1
                while heights[left] < height:
                    left += 1
            else:
                height = heights[right]
                right -=1
                while heights[right] < height:
                    right -=1

        return globalVolume