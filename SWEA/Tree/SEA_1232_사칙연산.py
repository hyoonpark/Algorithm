def postOrder(n):
    global S
    if n <= N:
        postOrder(n*2)
        postOrder(n*2+1)
        if tree[n] == '+':
            op2 = S.pop()
            op1 = S.pop()
            S.append(op1+op2)
        elif tree[n] == '-':
            op2 = S.pop()
            op1 = S.pop()
            S.append(op1-op2)
        elif tree[n] == '*':
            op2 = S.pop()
            op1 = S.pop()
            S.append(op1*op2)
        elif tree[n] == '/':
            op2 = S.pop()
            op1 = S.pop()
            S.append(op1/op2)
        else:
            S.append(int(tree[n]))



for tc in range(1, 11):
    N = int(input())
    tree = [0 for _ in range(N+1)]
    S = []
    for i in range(1, N+1):
        lst = list(input().split())
        tree[i] = lst[1]
    postOrder(1)
    ans = int(S.pop())
    print(f'#{tc}', ans)