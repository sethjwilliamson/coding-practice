class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        triangle = [[1]]
        
        for i in range(1, numRows):
            baseTriangle = [1 for x in range(i + 1)]
            
            if i > 1:
                for j in range(1, i):
                    baseTriangle[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
                    
            triangle.append(baseTriangle)
                
        return triangle