# tc 91

def Check(arr):
    global flag, ans
    cnt = 0

    for i in range(N+2):
        if flag:
            for j in range(N+2):
                if arr[i][j] == 'o':
                    cnt += 1
                else:
                    if cnt == 5:
                        flag = False
                        ans = 'YES'
                        break
                    else:
                        cnt = 0

def dgl(arr):
    global flag, ans
    cnt = 0

    for x in range(N+2):
        if flag:
            for i in range(N+2):
                if i+x <= N+1:
                    if arr[i][i+x] == 'o':
                        cnt += 1
                    else:
                        if cnt == 5:
                            flag = False
                            ans = 'YES'
                            break
                        else:
                            cnt = 0

    for x in range(N+2):
        if flag:
            for i in range(N+2):
                if i+x <= N+1:
                    if arr[i+x][i] == 'o':
                        cnt += 1
                    else:
                        if cnt == 5:
                            flag = False
                            ans = 'YES'
                            break
                        else:
                            cnt = 0

def dgl_t(arr):
    global flag, ans
    cnt = 0

    for x in range(N+2):
        if flag:
            for i in range(N+2):
                if N+1-i-x >= 0:
                    if arr[i][N+1-i-x] == 'o':
                        cnt += 1
                    else:
                        if cnt == 5:
                            flag = False
                            ans = 'YES'
                            break
                        else:
                            cnt = 0

    for x in range(N+2):
        if flag:
            for i in range(N+2):
                if N+1-i-x >= 0:
                    if arr[N+1-i-x][i] == 'o':
                        cnt += 1
                    else:
                        if cnt == 5:
                            flag = False
                            ans = 'YES'
                            break
                        else:
                            cnt = 0

for tc in range(1, int(input())+1):
    N = int(input())
    omok = [['.'] * (N+2)]+[['.']+list(input())+['.'] for _ in range(N)] + [['.'] * (N+2)]
    omok_t = list(map(list, zip(*omok)))
    ans = 'NO'
    flag = True
    Check(omok)
    Check(omok_t)
    dgl(omok)
    dgl_t(omok)

    print(f'#{tc}', ans)