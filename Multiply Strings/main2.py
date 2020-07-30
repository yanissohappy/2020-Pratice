class Solution(object):
    def multiply(self, num1, num2):
        # ord: 'c' -> 99
        # chr: 99 -> 'c'
        num1 = num1[::-1]
        num2 = num2[::-1]
        weight_1, weight_2 = 1, 1
        int_num1, int_num2 = 0, 0
        for i in range(len(num1)):
            int_num1 += weight_1 * (ord(num1[i]) - 48) # turn num into int
            weight_1 *= 10

        for i in range(len(num2)):
            int_num2 += weight_2 * (ord(num2[i]) - 48) # turn num into int
            weight_2 *= 10            
          
        mul = int_num1 * int_num2
        rev = []
        
        while True:
            rev.insert(0,chr(mul % 10 + 48))
            mul = mul // 10
            if mul == 0:
                break
                
        return (''.join(rev))