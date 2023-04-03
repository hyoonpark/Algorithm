# 1 무조건 4자리씩 출력하기
def binary(num):
    global result, cnt

    if num == 0:
        return result
    result[3-cnt] = str(num%2)
    num //= 2
    cnt += 1


for tc in range(1, int(input())+1):
    N, nums = input().split()
    alpha = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    ans = ''
    for n in nums:
        result = ['0'] * 4
        cnt = 0
        if n.isalpha():
            n = alpha.get(n)
            binary(n)
            ans += ''.join(result)
        else:
            binary(int(n))
            ans += ''.join(result)
    print(f'#{tc}', ans)

# 2 문제 조건과 동일하게 출력하기
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
    x = 4-(len(ans)%4)
    if x != 4:
        ans += '0' * x
    print(f'#{tc}', ans[::-1])

# 3 필요한 숫자만 출력하기
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
    print(f'#{tc}', ans[::-1])