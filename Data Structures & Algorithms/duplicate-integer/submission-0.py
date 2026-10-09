class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #so we accept a list of numbers, returning a  boolean if weve already seen it
        #well use a set and before we add, well check if its already in the dictionary

        s = set()

        for n in nums:
            if n in s:
                return True
            s.add(n)
        


        return False
        