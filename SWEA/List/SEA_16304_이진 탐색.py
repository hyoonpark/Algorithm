# 1
T = int(input())
for t in range(1, T+1):
    P, A, B = map(int, input().split())
    start = 1
    cntA = 0
    cntB = 0
    while start <= P:
        middle = int((start+P)/2)
        if middle == A:
            cntA += 1
            break
        elif middle > A:
            P = middle - 1
            cntA += 1
        else:
            start = middle + 1
            cntA += 1
    while start <= P:
        middle = int((start+P)/2)
        if middle == B:
            cntB += 1
            break
        elif middle > A:
            cntB += 1
            P = middle - 1
        else:
            cntB += 1
            start = middle + 1
    if cntA > cntB:
        print(f'#{t}', 'B')
    elif cntA < cntB:
        print(f'#{t}', 'A')
    else:
        print(f'#{t}', 0)

# 2
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