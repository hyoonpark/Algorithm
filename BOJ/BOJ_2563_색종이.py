N = int(input())    # 색종이 수
paper = [[0 for _ in range(100)] for _ in range(100)]    # 도화지
ans = 0
for _ in range(N):
    a, b = map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            paper[i][j] = 1
for c in paper:
    if 1 in c:
        ans += sum(c)
print(ans)