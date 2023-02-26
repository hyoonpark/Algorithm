def inOrder(n):
    global num
    if n <= N:
        inOrder(n*2)
        tree[n] = num
        num += 1
        inOrder(n*2+1)



for tc in range(1, int(input())+1):
    N = int(input())
    tree = [0] * (N+1)
    num = 1
    inOrder(1)
    root = tree[1]
    ans = tree[N//2]

    print(f'#{tc}', root, ans)