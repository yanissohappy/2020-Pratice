class Solution(object):
    def removeOuterParentheses(self, S):
        stack, ret = [], []
        
        left, right = 0, 0
        for parenthesis in S:
            if parenthesis == '(':
                left += 1
                stack.append(parenthesis)
            else:
                right += 1
                stack.append(parenthesis)
            
            if left == right:
                del stack[0]
                del stack[-1]
                ret.extend(stack)
                stack = []
                left, right = 0, 0
                
        return ''.join(ret)
                
                
        """ # 寫亂了  "(()())(())(()(()))" case 不對
        for parenthesis in S:
            if parenthesis != ')':
                stack.append(parenthesis)
            else:
                temp = []
                while len(stack) > 1:
                    popped_thing = stack.pop()
                    ret.append(popped_thing)
                    temp.append(popped_thing)
                ret.append(')' * len(temp))
                if len(stack) == 1:
                    stack.pop()
            print(stack, ''.join(ret))
        return ''.join(ret)
        """