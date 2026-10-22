class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums);
        longest_streak =  0;
        for s in mySet:
            if  (s - 1 ) not in mySet:
                current = s;
                current_streak = 1;


                while (current + 1) in mySet:
                    current += 1;
                    current_streak += 1;

                longest_streak = max(longest_streak, current_streak);                   

        return longest_streak;
        