from collections import defaultdict
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #we do +1 so that we can have len 3 and index 3
        myBucket = [ [] for _ in range (3)]

        for n in nums:
            myBucket[n].append(n)
        
        nums[:] = [val for bucket in myBucket for val in bucket]

        return nums;





        
        