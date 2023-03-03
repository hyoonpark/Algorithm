def Turn(idx):
    if swc[idx]:
        swc[idx] = 0
    else:
        swc[idx] = 1


N = int(input())    # 스위치 개수
swc = [0] + list(map(int, input().split()))    # 스위치 상태 표시
std = int(input())    # 학생수
for _ in range(std):
    i, j = map(int, input().split())
    if i == 1:    # 남자
        for k in range(1, N+1):
            if k % j == 0:
                Turn(k)
    elif i == 2:
        Turn(j)
        k = 1
        while 0<(j-k) and (j+k)<(N+1):
            if swc[j-k] == swc[j+k]:
                Turn(j-k)
                Turn(j+k)
                k += 1
            else:
                break

for s in range(1, len(swc)):
    if s%20 == 0:
        print(swc[s])
    else:
        print(swc[s], end=' ')