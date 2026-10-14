from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #need to loop through each string
        myMap = defaultdict(list)
        for string in strs:
            count = [0] * 26  # this will be  the fingerprint that all anagrams share
            for c in string:
                count[ord(c) - ord('a')] += 1 
            myMap[tuple(count)].append(string)

        return list(myMap.values())
