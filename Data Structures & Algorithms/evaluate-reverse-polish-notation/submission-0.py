class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        token_stack = []

        for ele in tokens:
            if ele not in ("+-*/"): 
                token_stack.append(ele)
            else:
                ele2 = token_stack.pop()
                ele1 = token_stack.pop()
                match ele:
                    case "+":
                        token_stack.append(int(ele1) + int(ele2))
                    case "-":
                        token_stack.append(int(ele1) - int(ele2))
                    case "*":
                        token_stack.append(int(ele1) * int(ele2))
                    case "/":
                        token_stack.append(int(int(ele1) / int(ele2)))

        return int(token_stack[0])



