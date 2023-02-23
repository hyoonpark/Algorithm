for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    num_lst = list(map(int, input().split()))
    add_num = 0
    sum_max = 0
    sum_min = 1000001
    for i in range(N-M+1):
        add_num = 0
        for j in range(i, i+M):
            add_num += num_lst[j]
        if add_num > sum_max:
            sum_max = add_num
        if add_num < sum_min:
            sum_min = add_num
    print(f'#{t}', sum_max-sum_min)