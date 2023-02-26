def postOrder(n):
    global num
    if n <= N:
        postOrder(n*2)
        postOrder(n*2+1)
        tree[n] = num
        num += 1



for tc in range(1, int(input())+1):
    N = int(input())
    tree = [0 for _ in range(N+1)]
    num = 1
    postOrder(1)

    root = tree[1]
    ans = tree[N//2]
    print(f'#{tc}', root, ans)