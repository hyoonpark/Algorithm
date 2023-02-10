T = int(input())
for t in range(1, T+1):
    N = int(input())
    cnts = [0] * 1001
    for _ in range(N):
        tp, A, B = map(int, input().split())
        cnts[A] += 1
        cnts[B] += 1
        if tp == 1:
            for i in range(A+1, B):
                cnts[i] += 1
        if tp == 2:
            if A % 2:
                for j in range(A+1, B):
                    if j % 2:
                        cnts[j] += 1
            else:
                for k in range(A+1, B):
                    if k % 2 == 0:
                        cnts[k] += 1
        if tp == 3:
            if A % 2:
                for l in range(A+1, B):
                    if l % 3 == 0 and l % 10 != 0:
                        cnts[l] += 1
            else:
                for m in range(A+1, B):
                    if m % 4 == 0:
                        cnts[m] += 1
    print(f'#{t}', max(cnts))