from py_compile import main


class validParenthesis:
    def isValid(self, s:str)-> bool:
        stack= []
        matching_brackets={')':'(',']':'[','}':'{'}
        for char in s:
            if char in '([{':
                stack.append(char)
            else:
                if len(stack)==0:
                    return False
                elif stack.pop()!=matching_brackets.get(char):
                    return False
                
        if len(stack)==0:
            return True
        else:
            return False
def main():
    sol=validParenthesis()
    s1="()"
    s2="()[]{}"
    s3="{[()]}"
    s4="(]"
    s5="]"
    s6="["
    print(sol.isValid(s1))
    
    print(sol.isValid(s2))
    
    print(sol.isValid(s3))
    
    print(sol.isValid(s4))
    
    print(sol.isValid(s5))
    
    print(sol.isValid(s6))

if __name__=="__main__":
    main()   
