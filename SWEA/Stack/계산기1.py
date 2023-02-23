def Calculation(String):
    S = []
    pString = ''  # 후위 표기식 문자열
    calcS = []

    for char in string:
        if not S and char == '+':
            S.append(char)
        elif S and char == '+':
            pString += S.pop()
            S.append(char)
        else:  # 숫자
            pString += char
    else:  # 마지막에 남아있는 연산자 빼주기 위해
        pString += S.pop()

    for char in pString:
        if char != '+':  # 숫자
            calcS.append(int(char))  # 정수타입으로 바꿔서 넣어준다
        elif char == '+':
            op2 = calcS.pop()
            op1 = calcS.pop()
            calcS.append(op1 + op2)  # 이 문제에서는 + 연산밖에 없지만 순서 주의

    ans = calcS.pop()
    return ans



for t in range(1, 11):
    str_len = int(input())  # 문자열 길이
    string = input()  # 중위 표기식 문자열

    print(f'#{t}', Calculation(string))