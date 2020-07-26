def isValid(s):
    stack = []
    i = 0
    if not s:
        return True
    if len(s) == 1:
        return False
    while i < len(s):
        if s[i] == '(' or s[i] == '{' or s[i] == '[':
            stack.append(s[i])
        else:
            stack.append(s[i])
            if stack:
                if len(stack) >= 2:
                    right_pop_char = stack.pop()
                    left_pop_char = stack.pop()
                    if left_pop_char == '(' and right_pop_char != ')':
                        return False
                    elif left_pop_char == '{' and right_pop_char != '}':
                        return False
                    elif left_pop_char == '[' and right_pop_char != ']':
                        return False
                else:
                    return False
        i += 1
    if not stack:
        return True
    else:
        return False

print(isValid("(([]){})"))
