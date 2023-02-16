def Calculation(String):

    S = []
    pString = ''    # 후위 표기식 문자열
    calcS = []
    top = -1

    for char in String:
        if not S and (char == '+' or char == '*'):
            S.append(char)
            top += 1
        elif S and char == '+':
            while S:
                pString += S.pop()
                top -= 1
            S.append(char)
            top += 1
        elif S and char == '*':
            if S[top] == '*':
                while S and S[top] != '+':
                    pString += S.pop()
                    top -= 1
                S.append(char)
                top += 1
            else:
                S.append(char)
                top += 1
        else:   # 숫자
            pString += char

    while S:
        pString += S.pop()

    for char in pString:
        if char == '*':
            op2 = calcS.pop()
            op1 = calcS.pop()
            result = op1 * op2
            calcS.append(result)
        elif char == '+':
            op2 = calcS.pop()
            op1 = calcS.pop()
            result = op1 + op2
            calcS.append(result)
        else:   # 숫자
            calcS.append(int(char))

    ans = calcS.pop()
    return ans



for t in range(1, 11):
    N = int(input())
    string = input()    # 중위 표기식 문자열

    print(f'#{t}', Calculation(string))