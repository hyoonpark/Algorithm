def Subtree(arr, n):
    global cnt
    for i in range(2):
        c = arr[i][n]
        if c != 0:
            cnt += 1
            Subtree(arr, c)


    return cnt



for tc in range(1, int(input())+1):
    E, N = map(int, input().split())  # 간선, 노드 번호
    n_lst = list(map(int, input().split()))
    tree = [[0 for _ in range(E + 2)] for _ in range(2)]
    cnt = 1    # 노드의 갯수 카운트
    for i in range(0, E * 2, 2):
        p, c = n_lst[i], n_lst[i + 1]  # 부모와 자식 노드 번호
        if tree[0][p] == 0:
            tree[0][p] = c
        else:
            tree[1][p] = c

    ans = Subtree(tree, N)
    print(f'#{tc}', ans)