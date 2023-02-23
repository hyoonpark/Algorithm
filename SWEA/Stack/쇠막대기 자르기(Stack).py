for t in range(1, int(input())+1):
    stack = input()
    S = []
    cuts = 0
    i = 0
    while i < len(stack):
        if stack[i] == '(' and stack[i+1] == ')':
            cuts += len(S)
            i += 2
        elif stack[i] == '(':
            S.append(stack[i])
            cuts += 1
            i += 1
        elif stack[i] == ')':
            S.pop()
            i += 1
    if len(S) == 0:
        print(f'#{t}', cuts)