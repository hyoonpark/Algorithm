for _ in range(1, 11):
    t = int(input())
    ladder = [[0 for _ in range(100)] for _ in range(100)]
    for n in range(100):
        ladder[n] = list(map(int, input().split()))
    print(ladder)