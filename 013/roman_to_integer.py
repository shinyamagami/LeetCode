class Solution:
    def romanToInt(self, s: str) -> int:
        length = len(s)
        result = 0
    
        last_letter = ""
        
        while length != 0:
            if s[0] == "M":
                if last_letter != "C":
                    result = result + 1000
                else:
                    result = result + 800
            
            if s[0] == "D":
                if last_letter != "C":
                    result = result + 500
                else:
                    result = result + 300
                    
            if s[0] == "C":
                if last_letter != "X":
                    result = result + 100
                else:
                    result = result + 80
                    
            if s[0] == "L":
                if last_letter != "X":
                    result = result + 50
                else:
                    result = result + 30
                    
            if s[0] == "X":
                if last_letter != "I":
                    result = result + 10
                else:
                    result = result + 8
                    
            if s[0] == "V":
                if last_letter != "I":
                    result = result + 5
                else:
                    result = result + 3  
            
            if s[0] == "I":
                result = result + 1  
            
            last_letter = s[0]
            s = s[1:]
            length = len(s)
            
        return result
