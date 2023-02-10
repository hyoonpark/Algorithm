N, M = map(int, input().split())
chr_lst = [['' for _ in range(N)] for _ in range(N)]
c = M//2
char = ''
for n in range(N):
    chr_lst[n] = list(input())
for i in range(N):
    char1 = ''
    char2 = ''
    for y in range(N-M):
        new_lst = chr_lst[y:M]
        # for j in range(c):
        #     char1 += new_lst[i][j]
        # for j in range(N-1, N-c-1, -1):
        #     char2 += new_lst[i][j]
        # if char1 == char2:
        #     for m in range(M):
        #         char += chr_lst[i][m]
        #     print(f'#{t}', char)
    print(new_lst)