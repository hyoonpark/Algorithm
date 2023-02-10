def binarySearch(P, key):
    start = 1
    end = P
    cnt = 0
    while start <= end:
        cnt += 1
        middle = int((start+end)/2)
        if middle == key:
            return cnt
        elif middle > key:
            end = middle
        else:
            start = middle

T = int(input())
for t in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    A = binarySearch(P, Pa)
    B = binarySearch(P, Pb)
    if A > B:
        print(f'#{t} B')
    elif A < B:
        print(f'#{t} A')
    else:
        print(f'#{t} 0')