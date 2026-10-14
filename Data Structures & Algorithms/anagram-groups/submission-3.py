from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #need to loop through each string
        myMap = defaultdict(list)
        for string in strs:
           sorted_string = tuple(sorted(string)) #sorted returns a list which cant be used a key
           myMap[sorted_string].append(string)

        return list(myMap.values())
