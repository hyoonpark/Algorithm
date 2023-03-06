# 방법1

for tc in range(1, int(input())+1):
    N = int(input())
    N_lst = list(map(int, input().split()))
    N_lst.sort()
    minV = 1000
    for i in range(N-2):
        for j in range(i+1, N-1):
            if N_lst[i] != N_lst[i+1] and N_lst[j] != N_lst[j+1]:
                A = i + 1
                B = j - i
                C = N - 1 -j
                if A*B*C != 0 and A<=N//2 and B<=N//2 and C<=N//2:
                    minV = min(minV, max(A, B, C)-min(A, B, C))
    if minV == 1000:
        ans = -1
    else:
        ans = minV
    print(f'#{tc}', ans)


# 방법2
for tc in range(1, int(input())+1):
    N = int(input())
    N_lst = list(map(int, input().split()))
    lst = [0] * (max(N_lst)+1)
    minV = 1000
    for n in N_lst:
        lst[n] += 1
    for i in range(len(lst)-2):
        for j in range(i+1, len(lst)-1):
            A = sum(lst[1:i+1])
            B = sum(lst[i+1:j+1])
            C = sum(lst[j+1:])
            if A*B*C != 0 and A<=N//2 and B<=N//2 and C<=N//2:
                minV = min(minV, max(A, B, C)-min(A, B, C))
    if minV == 1000:
        ans = -1
    else:
        ans = minV
    print(f'#{tc}', ans)