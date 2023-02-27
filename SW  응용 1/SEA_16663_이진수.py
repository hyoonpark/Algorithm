def Binary(num):
    global result, cnt
    if num == 0:
        return result
    result[3-cnt] = str(num%2)
    num //= 2
    cnt += 1
    Binary(num)



for tc in range(1, int(input())+1):
    N, hex = map(str, input().split())
    alpha = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    nums = ''
    for n in hex:
        result = ['0'] * 4
        cnt = 0
        if n.isalpha():
            val = alpha.get(n)
            Binary(val)
            nums += ''.join(result)
        else:
            Binary(int(n))
            nums += ''.join(result)

    print(f'#{tc}', nums)