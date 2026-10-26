class Solution:
    def isPalindrome(self, s: str) -> bool:
    
        s = s.lower();
        cleaned_text = "".join(char for char in s if char.isalnum())

        Left = 0;
        Right = len(cleaned_text) - 1;
        while(Left <= Right):
            if ( cleaned_text[Left] ==  cleaned_text[Right]):
                  Left+=1
                  Right-=1
            else:
                return False
                

        return True

          

        