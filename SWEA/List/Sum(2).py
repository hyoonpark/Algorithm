for _ in range(10):
    t = int(input())
    a_lst = [[0 for _ in range(100)] for _ in range(100)]
    for n in range(100):
        a_lst [n] = list(map(int, input().split()))
    max_num = 0
    for i in range(100):
        sum_num = 0
        for j in range(100):
            sum_num += a_lst[i][j]
        if sum_num > max_num:
            max_num = sum_num
    for j in range(100):
        sum_num = 0
        for i in range(100):
            sum_num += a_lst[i][j]
        if sum_num > max_num:
            max_num = sum_num
    sum_num = 0
    for i in range(100):
        sum_num += a_lst[i][i]
    if sum_num > max_num:
        max_num = sum_num
    sum_num = 0
    i = 0
    for j in range(99, -1, -1):
        sum_num += a_lst[i][j]
        i += 1
    if sum_num > max_num:
        max_num = sum_num
    print(f'#{t}', max_num)