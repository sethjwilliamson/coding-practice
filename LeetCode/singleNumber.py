class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        
        for i in nums:
            a ^= i
            
        return a
    
    
    def singleNumberHash(self, nums: List[int]) -> int:
        hashTable = {}
        
        for i in nums:
            try:
                hashTable.pop(i)
            except:
                hashTable[i] = 1
                
        return hashTable.popitem()[0]