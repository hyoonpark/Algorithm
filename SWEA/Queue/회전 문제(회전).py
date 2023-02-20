for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    num_lst = list(map(int, input().split()))

    for _ in range(M):
        temp = num_lst.pop(0)
        num_lst.append(temp)

    print(f'#{tc}', num_lst[0])