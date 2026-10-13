from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for str in strs:
            sortedString = tuple(sorted(str))
            result[sortedString].append(str)

        return list(result.values())
            

