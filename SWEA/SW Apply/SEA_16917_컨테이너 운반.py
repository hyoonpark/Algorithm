for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))    # 화물무게
    limit = list(map(int, input().split()))    # 적재용량
    weight.sort(reverse=True)    # 내림차순 정렬
    limit.sort(reverse=True)
    cnt = 0
    i = 0
    for w in weight:
        if i < M and limit[i] >= w:
            cnt += w
            i += 1
    print(f'#{tc}', cnt)


    # print(weight)
    # print(limit)