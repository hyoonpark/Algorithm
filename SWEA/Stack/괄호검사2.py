def Check(arr):
    S = []
    rslt = 0

    for char in arr:
        if char == '(' or char == '{':
            S.append(char)
        elif S and char == ')':
            if S.pop() != '(':
                return rslt
        elif S and char == '}':
            if S.pop() != '{':
                return rslt
        elif not S and (char == ')' or char == '}'):
            return rslt
    if not S:
        rslt = 1
        return rslt
    else:
        return rslt


for tc in range(1, int(input())+1):
    str_arr = input()   # 문자열 받아오기

    print(f'#{tc}', Check(str_arr))