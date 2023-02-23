def Check(Str):
    S = []
    rslt = 0

    for char in Str:
        if char == '(' or char == '{':
            S.append(char)
        elif S:
            if char == ')' and S.pop() != '(':
                return rslt
                break
            elif char == '}' and S.pop() != '{':
                return rslt
                break
        elif not S and (char == ')' or char == '}'):
            return rslt
            break
    if not S:
        rslt = 1
        return rslt
    else:
        return rslt



for tc in range(1, int(input())+1):
    Str = input()

    print(f'#{tc}', Check(Str))