from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #well use a map , each item in the list mapped to its frequencies
        #well then return the key whose value is k

        ourMap = defaultdict(int)
        for num  in nums:
            ourMap[num] += 1; #everytime we encounter our num we add one
        

        #lets sort by the values in desc and return a list
        sortedMap = dict(sorted(ourMap.items(), key=lambda item: item[1], reverse =True))
        #returns a list [(3,3), (2,2), (1, 1)]
        result = [];
        for i in range (k):
            element = list(sortedMap.keys())[i]
            result.append(element)
        
        return result;