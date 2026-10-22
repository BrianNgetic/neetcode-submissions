from collections import defaultdict
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      
        result = [1] * len(nums);
        

        preFix = 1;
        for i,v in enumerate(nums):
            result[i] = preFix;
            preFix *= nums[i];

        postFix = 1 
        for i in range(len(nums) - 1, -1, -1):
            result[i]  = result[i] * postFix;
            postFix *= nums[i]

        

            
        return result;