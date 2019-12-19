class Solution:
    def firstUniqChar(self, s: str) -> int:        
        charFound = False
        
        if len(s) == 1:
            return 0
        
        for i in range(0, len(s)):
            if charFound:
                return i - 1
            
            if s[i] == "*":
                continue
            
            for j in range(i + 1, len(s)):
                if s[i] == s[j]: 
                    break
                    
            
            if s[i] != s[j]:
                charFound = True
                
            
            s = s.replace(s[i], "*")
            #print(s)
            
        if charFound:
            return i
            
        return -1