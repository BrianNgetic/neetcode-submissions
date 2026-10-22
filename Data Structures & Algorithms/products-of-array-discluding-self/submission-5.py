class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_co = 0
        res = []

        for num in nums:
            if num == 0:
                zero_co += 1
            else:
                prod *= num
            
        if zero_co > 1:
            return [0] * len(nums)
        
        for num in nums:
            if zero_co:
                res.append( 0 if num != 0 else prod)
            else:
                res.append( prod // num )
        
        return res