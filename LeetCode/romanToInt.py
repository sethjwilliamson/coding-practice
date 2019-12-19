class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        
        for i in range(len(s)):
            positive = True
            
            if s[i] == "I":
                for j in range(i + 1, i + 4):
                    if j < len(s):
                        if s[j] == "V":
                            positive = False
                        elif s[j] == "X":
                            positive = False
                    else: 
                        break
                if positive:
                    total += 1
                else:
                    total -= 1
            elif s[i] == "X":
                for j in range(i + 1, i + 4):
                    if j < len(s):
                        if s[j] == "L":
                            positive = False
                        elif s[j] == "C":
                            positive = False
                    else: 
                        break
                if positive:
                    total += 10
                else:
                    total -= 10
            elif s[i] == "C":
                for j in range(i + 1, i + 4):
                    if j < len(s):
                        if s[j] == "D":
                            positive = False
                        elif s[j] == "M":
                            positive = False
                    else: 
                        break
                if positive:
                    total += 100
                else:
                    total -= 100
            else:
                if s[i] == "V":
                    total += 5
                elif s[i] == "L":
                    total += 50
                elif s[i] == "D":
                    total += 500
                else:
                    total += 1000
            
        return total