N, M, L = map(int, input().split())
p_lst = [1] + [0]*(N-1)
cnt = 1
i = 0
while M not in p_lst:
    cnt += 1
    if p_lst[i]%2:
        i = (i+L) % N
        p_lst[i] += 1
    else:
        if (i-L)%N >= 0:
            i = (i-L)%N
            p_lst[i] += 1
        else:
            i = N - (abs(i-L)%N)
            if i == N:
                i = 0
                p_lst[i] += 1
ans = cnt - 1
print(ans)