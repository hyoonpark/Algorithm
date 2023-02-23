def maxLen():
    max_len = 0

    for i in range(N):
        length = 0
        for j in range(M):
            if row_lst[i][j] == '1':
                length += 1
                if length > max_len:
                    max_len = length
            else:
                if length > max_len:
                    max_len = length
                length = 0

    for j in range(M):
        length = 0
        for i in range(N):
            if row_lst[i][j] == '1':
                length += 1
                if length > max_len:
                    max_len = length
            else:
                if length > max_len:
                    max_len = length
                length = 0

    return max_len



for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    row_lst = [list(input().split()) for _ in range(N)]

    print(f'#{tc}', maxLen())