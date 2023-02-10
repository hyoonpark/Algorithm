for t in range(1, int(input())+1):
    N = int(input())
    num_lst = [[0 for _ in range(N)] for _ in range(N)]
    for n in range(N):
        num_lst[n] = list(map(int, input().split()))
    print(f'#{t}')
    for x in range(N):
        for j in range(x, x+1):
            for i in range(N-1, -1, -1):
                print(num_lst[i][j], end='')
            print(end=' ')
        for i in range(N-x-1, N-x-2, -1):
            for j in range(N-1, -1, -1):
                print(num_lst[i][j], end='')
            print(end=' ')
        for j in range(N-x-1, N-x-2, -1):
            for i in range(N):
                print(num_lst[i][j], end='')
        print()