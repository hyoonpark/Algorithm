def Forth(String):
    char = ''
    S = []
    ans = 0
    for char in String:
        if char == '.':
            ans = S.pop()
            if S:
                return f'error'
            else:
                return ans
            break
        elif char.isdigit():
            S.append(int(char))
        else:
            if not S:
                return f'error'
                break
            else:
                op2 = S.pop()
                if not S:
                    return f'error'
                    break
                else:
                    op1 = S.pop()
                    if char == '+':
                        ans = op1 + op2
                    elif char == '-':
                        ans = op1 - op2
                    elif char == '*':
                        ans = op1 * op2
                    elif char == '/':
                        ans = (op1 // op2)
                    S.append(ans)




for t in range(1, int(input())+1):
    string = input().split()
    print(f'#{t}', Forth(string))