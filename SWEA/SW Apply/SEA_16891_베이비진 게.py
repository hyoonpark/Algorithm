def check(lst):
    j = 0
    rslt = 0
    while j < 10:
        if lst[j] >= 3:
            rslt += 1
            return rslt
        if lst[j] >= 1 and lst[j+1] >= 1 and lst[j+2] >= 1:
            rslt += 1
            return rslt
        j += 1
    return rslt



for tc in range(1, int(input())+1):
    num_lst = list(map(int, input().split()))
    pl1 = [0] * 12
    pl2 = [0] * 12
    for i in range(0, 11, 2):
        pl1[num_lst[i]] += 1
        pl2[num_lst[i+1]] += 1
        cnt = check(pl1)
        if cnt > 0:
            ans = 1
            break
        cnt = check(pl2)
        if cnt > 0:
            ans = 2
            break
    else:
        ans = 0
    print(f'#{tc}', ans)