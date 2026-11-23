class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
      
        for sublist in matrix:
            left = 0;
            right = len(sublist)  - 1 
            
            if target > sublist[right]:
                continue
            else:
               

                while left <= right:
                    mid = (left + right) // 2
                    if target < sublist[mid]:
                        right  = mid - 1
                    elif target > sublist[mid]:
                        left = mid + 1
                    else:
                        return True
        

        return False
