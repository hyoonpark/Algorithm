N = int(input())    # 스위치 개수
swc = [0] + list(map(int, input().split()))    # 스위치 상태 표시
std = int(input())    # 학생수
for _ in range(std):
    i, j = map(int, input().split())
    if i == 1:
        