from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #given an integer array nums length n,  we want to return the top 2 most repeating elements
        #if k is 2

        #we know that each number repeats at least once and at most len(nums)
        #first lets map each number to how many times it repeats
        myMap = defaultdict(int)

        for num in nums:
            myMap[num] += 1;

            #[1, 2,2,2,2, 3,3]
            #{1: 1, 2: 4, 3: 2}

        #next lets initialize an array of list, length len +1
        #at index 1, we will have all the numbers that repeated once .. till index n+1 (len(nums))

        myBucket = [ [] for _ in range (len(nums) + 1)];
  
        

        for key, v in myMap.items():
            myBucket[v].append(key);

        result = []

        for sublist in reversed(myBucket):
            for num in sublist:
                result.append(num);
                if len(result) == k:
                    return result;


    
