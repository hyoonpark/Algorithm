def Calculation(String):

    S = []
    pStr = ''
    calcS = []
    top = -1

    for char in String:
        if char == '(':
            S.append(char)
            top += 1
        elif not S and (char == '+' or char == "*"):
            S.append(char)
            top += 1
        elif S and char == ')':
            while S[top] != '(':
                pStr += S.pop()
                top -= 1
            S.pop()
            top -= 1
        elif S and char == '+':
            while S and S[top] != '(':
                pStr += S.pop()
                top -= 1
            S.append(char)
            top += 1
        elif S and char == '*':
            while S and S[top] == '*':
                pStr += S.pop()
                top -= 1
            S.append(char)
            top += 1
        else:
            pStr += char
    while S:
        pStr += S.pop()

    for char in pStr:
        if char == '*':
            op2 = calcS.pop()
            op1 = calcS.pop()
            calcS.append(op1*op2)
        elif char == '+':
            op2 = calcS.pop()
            op1 = calcS.pop()
            calcS.append(op1+op2)
        else:
            calcS.append(int(char))

    return calcS.pop()



for tc in range(1, 11):
    N = int(input())
    Str = input()

    print(f'#{tc}', Calculation(Str))