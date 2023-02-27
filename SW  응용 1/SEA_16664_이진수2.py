for tc in range(1, int(input())+1):
    N = float(input())
    result = ''
    while True:
        val = N * 2
        flo_lst = [int(num) for num in str(val)[2:]]
        if sum(flo_lst) != 0:
            result += str(int(N * 2))
            if int(N * 2) == 0:
                N = float('0.' + str(val)[2:])
            else:
                N = N * 2 - 1
        else:
            result += '1'
            print(f'#{tc}', result)
            break
        if len(result) > 12:
            print(f'#{tc} overflow')
            break