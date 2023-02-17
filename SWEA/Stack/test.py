for tc in range(1, int(input()) + 1):
    w_lst = input()
    stk = []

    for i in w_lst:
        if i in '({':
            stk.append(i)
        elif i in ')}':
            if stk and i == ')' and stk[-1] == '(':
                stk.pop()
            elif stk and i == '}' and stk[-1] == '{':
                stk.pop()
    if not len(stk):
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')