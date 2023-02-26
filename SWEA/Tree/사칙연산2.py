def postorder(v):
    global arr
    if not v:
        return
    postorder(L[v])
    postorder(R[v])
    arr.append(tree[v])


def cal(lst):
    stack = []
    while lst:
        val = lst.pop(0)
        if val in symbol:
            a = stack.pop()
            b = stack.pop()
            if val == '+':
                stack.append(b + a)
            elif val == '-':
                stack.append(b - a)
            elif val == '*':
                stack.append(b * a)
            else:
                stack.append(b // a)
        else:
            stack.append(int(val))
    return stack[0]


symbol = ['+', '-', '*', '/']
for tc in range(1, 11):
    N = int(input())
    L = [0] * (N + 1)
    R = [0] * (N + 1)
    tree = [0] * (N + 1)
    for _ in range(N):
        temp = list(map(str, input().split()))
        i = int(temp[0])
        tree[i] = temp[1]
        if len(temp) >= 3:
            L[i] = int(temp[2])
        if len(temp) == 4:
            R[i] = int(temp[3])
    arr = []
    postorder(1)
    print('#{} {}'.format(tc, cal(arr)))