for t in range(1, int(input())+1):
    N = int(input())
    S = [1]
    print(f'#{t}')
    print(*S)
    for _ in range(1, N):
        stack = [0] + S + [0]  # 맨 처음과 끝에는 1 밖에 없으므로 0을 붙여준다
        S = []
        num1 = stack.pop()

        while stack:
            num2 = stack.pop()
            S.append(num1 + num2)
            num1 = num2
        print(*S)
