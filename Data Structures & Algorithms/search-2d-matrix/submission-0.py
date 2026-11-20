class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for sublist in matrix:
            left = 0;
            right = len(sublist) - 1;
            if sublist[right] < target:
                continue;
            else:
                while left <= right:
                    mid = (left + right ) // 2;
                    if sublist[mid] > target:
                        right = mid - 1
                    elif sublist[mid] < target:
                        left = mid + 1
                    else:
                        return True
                    
        
        return False
            

        