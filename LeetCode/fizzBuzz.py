class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        array = []
        
        for i in range(1, n + 1):
            string = ""
            
            if i % 3 == 0:
                string = "Fizz"
            if i % 5 == 0:
                string += "Buzz"
            
            if string == "":
                string = str(i)
                
            array.append(string)
            
        return array