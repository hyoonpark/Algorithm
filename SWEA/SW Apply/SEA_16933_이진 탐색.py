def bi_search(arr, num):

    s = 0
    e = N-1
    m = (s+e)//2
    x = 0
    while s <= e:
        if num < arr[m]:
            if x == -1:
                return False
            x -= 1
            e = m-1
            m = (s+e)//2
        elif num > arr[m]:
            if x == 1:
                return False
            x += 1
            s = m+1
            m = (s+e)//2
        elif num == arr[m]:
            return True
    return False


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    cnt = 0
    for b in B:
        flag = bi_search(A, b)
        if flag:
            cnt += 1
    print(f'#{tc}', cnt)