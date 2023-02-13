def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b-1)

for _ in range(10):
    t = int(input())
    a, b = map(int, input().split())
    print(f'#{t}', power(a, b))