class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 1. Correctly sort in place
        solution = []  # 2. Start with a truly empty list
        
        for i in range(len(nums)):
            # LEVEL 1: Skip duplicate starting numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum > 0:
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    # Found a valid triplet!
                    solution.append([nums[i], nums[left], nums[right]])
                    
                    # LEVEL 2: Skip duplicates for left and right pointers
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Always move both pointers inward after finding a match
                    left += 1
                    right -= 1
                    
        return solution
