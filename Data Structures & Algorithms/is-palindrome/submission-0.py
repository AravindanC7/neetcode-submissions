class Solution:
    def isPalindrome(self, s: str) -> bool:
        char = "".join(ch.lower() for ch in s if ch.isalnum())
        l,r = 0,len(char)-1

        while l<r:
            if char[l]== char[r]:
                l+=1
                r-=1
            else:
                return False
        return True



        