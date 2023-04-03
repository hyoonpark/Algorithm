for tc in range(1, int(input())+1):
    N, nums = input().split()
    num = int(nums, 16)
    ans = ''
    while num != 0:
        a = num%2
        if a >= 10:
            ans += chr(a+55)
        else:
            ans += str(a)
        num //= 2
    x = 4-len(ans)%4
    if x != 4:
        ans += '0'*x
    print(f'#{tc}', ans[::-1])