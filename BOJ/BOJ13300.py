N, K = map(int, input().split())
grdM = [0 for _ in range(7)]
grdW = [0 for _ in range(7)]
cnt = 0
for _ in range(N):
    S, G = map(int, input().split())
    if S:
        grdM[G] += 1
    else:
        grdW[G] += 1
for i in range(1, 7):
    if grdM[i]%K:
        cnt += (grdM[i]//K + 1)
    else:
        cnt += grdM[i]//K
    if grdW[i]%K:
        cnt += (grdW[i]//K + 1)
    else:
        cnt += grdW[i]//K

print(cnt)