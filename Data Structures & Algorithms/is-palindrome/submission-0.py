class Solution:
    def isPalindrome(self, s: str) -> bool:
    

        cleaned_text = "".join(char for char in s if char.isalnum())

        Left = 0;
        Right = len(cleaned_text) - 1;
        while(Left <= Right):
            if ( cleaned_text[Left].lower() ==  cleaned_text[Right].lower()):
                  Left+=1
                  Right-=1
            else:
                return False
                

        return True

          

        