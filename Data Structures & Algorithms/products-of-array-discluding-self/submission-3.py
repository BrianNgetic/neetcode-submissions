from collections import defaultdict
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        inFix = [1] * (len(nums));
        postFix = [1] * (len(nums));
        

        tmp1 = 1;
        for i,v in enumerate(nums):
            inFix[i] = tmp1;
            tmp1 *= nums[i];

        tmp2  =1 
        for i in range(len(nums) - 1, -1, -1):
            postFix[i] = tmp2;
            tmp2 *= nums[i]

        

        result = [1] * len(nums);

        for i in range(len(nums)):
            result[i] = inFix[i] * postFix[i];

        

            
        return result;