String = '3+4+5*6+7'
S = []
pString = ''    # 후위 표기식 문자열
calcS = []
top = -1

for char in String:
    if not S and (char == '+' or char == '*'):
        S.append(char)
        top += 1
    elif S and char == '+':
        pString += S.pop()
        top -= 1
        S.append(char)
        top += 1
    elif S and char == '*':
        if S[top] == '*':
            pString += S.pop()
            top -= 1
            S.append(char)
            top += 1
        else:
            S.append(char)
            top += 1
    else:   # 숫자
        pString += char
else:
    pString += S.pop()
print(pString)