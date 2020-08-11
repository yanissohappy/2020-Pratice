class Solution(object):
    def removeSpace(self, string):
        i = 0
        ret = []
        while i < len(string):
            if string[i] == ' ':
                i += 1
                continue
            else:
                ret.append(string[i])            
            i += 1
        return str(''.join(ret))
            
    
    def binaryCalculate(self, stack):
        if not ('+' in stack or '-' in stack):
            return int(''.join(stack))
        while '+' in stack or '-' in stack:
            latter_num = []
            fore_num = []
            while len(stack) >= 1 and (stack[0] != '+' and stack[0] != '-' and stack[0] !=  '/' and stack[0] != '*'):
                fore_num.append(stack.pop(0))
            sign = stack.pop(0)
            while len(stack) >= 1 and (stack[0] != '+' and stack[0] != '-' and stack[0] !=  '/' and stack[0] != '*'):
                latter_num.append(stack.pop(0))
            if sign == '+':
                stack.insert(0, str( int(''.join(fore_num)) + int(''.join(latter_num))))
            else:
                stack.insert(0, str( int(''.join(fore_num)) - int(''.join(latter_num))))
        return int(stack[0])
            
    
    def calculate(self, s):
        stack = []
        i = 0
        s = self.removeSpace(s)
        print(s)
        while i < len(s):
            if s[i] == '/' or s[i] == '*':
                latter_num = []
                sign = s[i] 
                fore_num = []                
                while i + 1 < len(s) and (s[i + 1] != '+' and s[i + 1] != '-' and s[i + 1] != '/' and s[i + 1] != '*'):
                    latter_num.append(s[i + 1])
                    i += 1
                while len(stack) >= 1 and (stack[-1] != '+' and stack[-1] != '-' and stack[-1] !=  '/' and stack[-1] != '*'):
                    fore_num.insert(0, stack.pop())
                
                if sign == '/':
                    stack.append(str(int( int(''.join(fore_num)) / int(''.join(latter_num)))))
                else:
                    stack.append(str(int( int(''.join(fore_num)) * int(''.join(latter_num)))))
                i += 1
                continue
            stack.append(s[i])
            i += 1
        return self.binaryCalculate(stack)