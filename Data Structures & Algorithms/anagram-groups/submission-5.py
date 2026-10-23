from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myMap = defaultdict(list)
        for string in strs:
            kArr = [0] * 26;
            for char in string:
                kArr[ord(char) - ord('a')] += 1;
            myMap[tuple(kArr)].append(string); #had to be a tuple since a list cant be a key
        


        return list(myMap.values());

