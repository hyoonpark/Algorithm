'''
0. 규칙을 찾았는데 코드가 길어질 것 같다? 그냥 진행시켜.
1. 반례가 없도록 정성코딩 해준다.
'''

K = int(input())    # 제곱미터당 참외 수
full_h = 0
full_w = 0
sub_h = 0
sub_w = 0
leng = []
for _ in range(6):
    i, j = map(int, input().split())
    if i == 1 or i == 2:
        if j >= full_h:
            full_h = j
    elif i == 3 or i == 4:
        if j >= full_w:
            full_w = j
    leng.append((i, j))
for l in range(5):
    if leng[l][0] == 1 and leng[l+1][0] == 3:
        sub_w, sub_h = leng[l][1], leng[l+1][1]
    elif leng[l][0] == 4 and leng[l+1][0] == 1:
        sub_w, sub_h = leng[l+1][1], leng[l][1]
    elif leng[l][0] == 2 and leng[l+1][0] == 4:
        sub_w, sub_h = leng[l][1], leng[l+1][1]
    elif leng[l][0] == 3 and leng[l+1][0] == 2:
        sub_w, sub_h = leng[l][1], leng[l+1][1]
else:
    if leng[0][0] == 3 and leng[-1][0] == 1:
        sub_h, sub_w = leng[0][1], leng[-1][1]
    elif leng[0][0] == 1 and leng[-1][0] == 4:
        sub_h, sub_w = leng[-1][1], leng[0][1]
    elif leng[0][0] == 4 and leng[-1][0] == 2:
        sub_h, sub_w = leng[0][1], leng[-1][1]
    elif leng[0][0] == 2 and leng[-1][0] == 3:
        sub_h, sub_w = leng[-1][1], leng[0][1]
ans = ((full_w*full_h) - (sub_w*sub_h)) * K
print(ans)