class Solution:
    def isOpen(self, c: str) -> bool:
        return c == '(' or c == '{' or c == '['
    
    def isClose(self, c: str) -> bool:
        return c == ')' or c == '}' or c == ']'

    def isSameType(self, a: str, b: str) -> bool:
        match a:
            case '(' | ')':
                return b == '(' or b == ')'
            case '{' | '}':
                return b == '{' or b == '}'
            case '[' | ']':
                return b == '[' or b == ']'
            case _:
                return False
    
    def isValid(self, s: str) -> bool:
        end = len(s)-1
        stack = list()

        print(len(s))
        print("end:", end)


        if(len(s) % 2 != 0):
            return False
        if(s[0] == ')' or s[0] == '}' or s[0] == ']'):
            return False
        if(s[end] == '(' or s[end] == '{' or s[end] == '['):
            return False

        for i in range(len(s)):
            print("idx: ", i)
            if(i == 0 and self.isOpen(s[i])):
                stack.append(s[i])
                continue

            top = stack[len(stack)-1] if len(stack) > 0 else None
            cur = s[i]

            if(self.isOpen(cur)):
                print('isopen')
                stack.append(cur)
            elif(self.isClose(cur)):
                print('isclose')
                print(top, cur)
                if(len(stack) != 0 and self.isSameType(top,cur)):
                    stack.pop()
                else:
                    return False

        print("final check: ", len(stack))
        return len(stack) == 0


    
