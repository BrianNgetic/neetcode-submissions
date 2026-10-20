class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * (len(nums));

        # index = 1;

        prefix = 1;
        for i in range(len(nums)):
            # if(i == 0):
            #    continue;
              
            
            result[i] = prefix;
            prefix = prefix * nums[i]
    
        postfix = 1;
        for i, item in reversed(list(enumerate(nums))):
            result[i] = result[i] * postfix;
            postfix = postfix * nums[i];

        return result;