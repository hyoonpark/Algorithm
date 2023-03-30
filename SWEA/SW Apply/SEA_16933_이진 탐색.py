def bi_search(arr, num):
    global cnt
    s = 0
    e = N-1
    m = (s+e)//2
    x = 0
    while s <= e:
        if num < arr[m]:
            if x == -1:
                break
            x = -1
            e = m-1
            m = (s+e)//2
        elif num > arr[m]:
            if x == 1:
                break
            x = 1
            s = m+1
            m = (s+e)//2
        elif num == arr[m]:
            cnt += 1
            return cnt



for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    cnt = 0
    for b in B:
        bi_search(A, b)

    print(f'#{tc}', cnt)