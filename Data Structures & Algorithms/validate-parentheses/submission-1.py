class Solution:
    def isValid(self, s: str) -> bool:
        parens = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                parens.append(c)
            else:
                if len(parens) == 0: return False
                if parens[-1] == '(' and c == ')':
                    parens.pop()
                elif parens[-1] == '{' and c == '}':
                    parens.pop()
                elif parens[-1] == '[' and c == ']':
                    parens.pop()
                else:
                    return False
        return len(parens) == 0
                    
                
