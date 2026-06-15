class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0;
        j = len(s)-1
        s = s.lower()

        while i < j:
            if not s[i].isalnum():
                i = i+1
                continue
            if not s[j].isalnum():
                j = j-1
                continue
            if s[i].isalnum() and s[j].isalnum() and s[i]!=s[j]:
                return False
            i = i+1
            j = j-1
        return True