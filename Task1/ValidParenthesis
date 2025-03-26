class Solution:
    def isValid(self, s):
        pairing = {']': '[', '}': '{', ')': '('} 
        array = []

        for char in s:
            if char in pairing.values():  # If it's an opening bracket
                array.append(char)
            elif char in pairing.keys():  # If it's a closing bracket
                if array and array[-1] == pairing[char]:
                    array.pop()
                else:
                    return False
            else:
                return False  
        
        return not array  
