T = int(input())

for i in range(1, T+1):
    D, A, B, F = map(int, input().split())
    t = D / (A+B)
    F_distance = F * t
    print(f'#{i}', F_distance)