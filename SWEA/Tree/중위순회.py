def inOrder(node):
    global char

    if node <= N:
        inOrder(node*2)
        char += tree[node]
        inOrder(node*2+1)

    return char


for tc in range(1, 11):
    N = int(input())
    tree = ['' for _ in range(N+1)]
    char = ''
    for i in range(1, N+1):
        arr = list(input().split())
        tree[i] = arr[1]

    ans = inOrder(1)
    print(f'#{tc}', ans)