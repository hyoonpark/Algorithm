'''
0. 남자, 여자를 나누고 인덱스를 이용해 학년별로 리스트를 만들 수 있다.
1. 남녀 6학년까지 리스트를 만들어준다.
2. 성별과 학년을 반복문으로 받아서 각 학년의 인덱스에 인원을 추가해준다.
3. 학년별로 인원수를 확인하고 필요한 방의 갯수를 센다.
'''


N, K = map(int, input().split())    # 인원수, 배정 최대
grdM = [0 for _ in range(7)]    # 남자 학년 리스트
grdW = [0 for _ in range(7)]    # 여자 학년 리스트
cnt = 0    # 방 갯수
for _ in range(N):
    S, G = map(int, input().split())
    if S:    # 남자
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