def Tree(i):
    left = i*2
    right = i*2+1
    if left < N:
        if tree[left] == 0:
            Tree(left)
    if right < N:
        if tree[right] == 0:
            Tree(right)
    if left <= N and right <= N:
        tree[i] = tree[left] + tree[right]
    elif left <= N:
        tree[i] = tree[left]



for tc in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    for _ in range(M):
        n, c = map(int, input().split())
        tree[n] = c

    Tree(1)
    print(f'#{tc}', tree[L])

    x <= N
    CAa()
    xc()