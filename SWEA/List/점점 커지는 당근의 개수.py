T = int(input())

for t in range(1, T+1):
    N = int(input())
    C = list(map(int, input().split()))
    cnt = 1
    cnt_lst = [1]
    for i in range(N-1):
        if C[i] + 1 == C[i+1]:
            cnt += 1
            cnt_lst.append(cnt)
        else:
            cnt = 1
            cnt_lst.append(cnt)

    print(f'#{t}', max(cnt_lst))
