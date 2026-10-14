from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #we are going to use a dictionary, the key being the index
        #the value being the target - nums[index]
        myMap = defaultdict(int)
        for index, value in enumerate(nums):
            complement = target - value;
            
            if complement in myMap:
                return[myMap[complement], index]

            myMap[value] = index