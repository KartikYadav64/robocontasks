import math

class Solution:
    def generate(self, numRows):
        answer = []
        
        for i in range(numRows):
            row = []
            for j in range(i + 1):
                binomial_coefficient = math.factorial(i) // (math.factorial(j) * math.factorial(i - j))
                row.append(binomial_coefficient)
            answer.append(row)
        
        return answer
