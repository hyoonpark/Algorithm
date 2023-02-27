'''
0. SWEA에 있는 색칠하기와 매우 유사. 그것보다 과목평가2회차? 문제랑 똑같다고 생각.
1. 색종이 정보를 통해 배열을 N번째 색종이는 n으로 바꿔준다.
2. 똑같이 반복문을 돌려 N번째 색종이가 얼마나 차지하고 있는지 count 메서드를 사용해 출력한다.
'''

N = int(input())
crd = [[0]*1001 for _ in range(1001)]
for n in range(1, N+1):
    x, y, b, h = map(int, input().split())    # 열, 행, 너비, 높이
    for i in range(y, y+h):
        for j in range(x, x+b):
            crd[i][j] = n
for n in range(1, N+1):
    ans = 0
    for arr in crd:
        if sum(arr):
            ans += arr.count(n)
    print(ans)