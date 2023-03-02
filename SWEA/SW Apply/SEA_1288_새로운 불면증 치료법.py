for tc in range(1, int(input())+1):
    N = int(input())
    num_lst = []
    for i in range(1, 100):
        sn = str(N*i)
        for s in sn:
            num_lst.append(s)
        lst = list(set(num_lst))
        if len(lst) == 10:
            rslt = i
            break
    ans = rslt * N
    print(f'#{tc}', ans)