for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    cz = [0] + list(map(int, input().split()))    # 치즈양
    pot = [i for i in range(1, N+1)]    # 피자번호, 큐처럼 사용예정
    idx = N+1    # M개 들어가고 남은것 초기값

    while len(pot) > 1:    # 하나 남을때까지 돌려돌려
        num = pot.pop(0)
        cz[num] = cz[num] // 2
        if cz[num]:    # 치즈가 남아있으면
            pot.append(num)
        else:    # 치즈 다 녹았당
            if idx <= M:
                pot.append(idx)
                idx += 1

    print(f'#{tc}', pot[0])
