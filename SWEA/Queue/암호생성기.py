for _ in range(10):
    tc = int(input())
    pw_lst = list(map(int, input().split()))    #
    if min(pw_lst)%15:
        cir = min(pw_lst)//15
    else:
        cir = (min(pw_lst)//15) - 1
    for i in range(8):
        pw_lst[i] -= cir * 15
    while pw_lst[-1] != 0:
        for i in range(1, 6):
            if pw_lst[0] - i < 0:
                pw_lst.pop(0)
                pw_lst.append(0)
            else:
                pw_lst.append(pw_lst.pop(0) - i)
            if pw_lst[-1] == 0:
                break

    print(f'#{tc}', *pw_lst)