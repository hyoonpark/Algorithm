tc = int(input())
for _ in range(tc):
    n, lst = input().split()
    n = int(n)
    for char in lst:
        print(char*n, end='')
    print()