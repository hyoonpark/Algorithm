def Calc(node):
    global S
    if node <= N:
        Calc(node*2)
        Calc(node*2+1)
        if tree[node] == '+':
            op2 = S.pop()
            op1 = S.pop()
            S.append(op1+op2)
        elif tree[node] == '-':
            op2 = S.pop()
            op1 = S.pop()
            S.append(op1-op2)
        elif tree[node] == '*':
            op2 = S.pop()
            op1 = S.pop()
            S.append(op1*op2)
        elif tree[node] == '/':
            op2 = S.pop()
            op1 = S.pop()
            S.append(op1/op2)
        else:
            S.append(int(tree[node]))




for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N+1)
    S = []
    for i in range(1, N+1):
        elem = list(input().split())
        tree[i] = elem[1]

    Calc(1)
    ans = int(S[0])
    print(f'#{tc}', ans)