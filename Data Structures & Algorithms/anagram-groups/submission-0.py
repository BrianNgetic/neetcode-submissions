from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for string in strs:
            charCount = [0] * 26
            for char in string:
                charCount[ord(char) - ord('a')] += 1

            result[tuple(charCount)].append(string)
            
        return list(result.values())
            

