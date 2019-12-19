class Solution:
    import re
    
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'\W+', '', s)
        
        return s.lower() == s[::-1].lower()