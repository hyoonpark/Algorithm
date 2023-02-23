for t in range(1, int(input())+1):
    N = int(input())
    a_lst = [0 for _ in range(10)]
    num_lst = list(map(int, input()))
    ans = 0
    idx = 0
    for n in num_lst:
        a_lst[n] += 1
    for i in range(10):
        if a_lst[i] >= ans:
            ans = a_lst[i]
            idx = i
    print(f'#{t}', idx, ans)