
from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #our input is one list , nums, and a target interger
        #we dont reutnr the values that make up our integer but rather their indexes

        #we will use a hashmap
        #The key of the hashmap will be the index, the value will be target - num[index]
                #so for example in our first the map will be {0: 4, 1: 3}
                #once we have the first key value pair, well check the list if the value exists, if 
                 #   s o we return the index
        
        ourMap = defaultdict(int)

        for i, v in enumerate(nums):
           
            if v in ourMap:
                return [ourMap[v], i]
                #the problem here,is instead of our value j in the return list  [i, j] being the index of the 
                #first value(the  key found in the map), it should be the index of hte current 
            else:   
                                                        #{3, 4, 5, 6} target  = 7
                ourMap[target - v] =  i #first iteration, {4.0} {3.1}} so on

         