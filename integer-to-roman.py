class Solution:

            
    d = {
        'M': {"value": 1000},
        'D': {"value": 500},
        
        'C': {"value": 100},
        'L': {"value" : 50},
        
        'X': {"value" : 10},
        'V': {"value" : 5},
        
        'I': {"value" : 1},



    }
    
    
    def resolve(self, num):
        
            
        for k, v in self.d.items():
            if num == v['value']:
                num -= num - v['value']
                return k, num
                               

                
        
        
    def intToRoman(self, num: int) -> str:        
        
        r = ''
        while num != 0:
            l, num = self.resolve(num)
            r = r + l
        
        return r
            
