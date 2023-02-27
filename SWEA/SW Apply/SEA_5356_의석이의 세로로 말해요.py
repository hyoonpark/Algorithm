'''
0. 배열을 세로로 읽을 수 있다. 문자열을 더해서 출력할 수 있다.
1. 문자열을 배열로 받아온다.
2. 받아온 문자열 중 가장 긴 것을 찾아 mx값에 넣어준다.
3. 각 행의 길이에 맞게 조건을 주어 세로로 읽어준다.
'''

for tc in range(1, int(input())+1):
    str_lst = [list(input()) for _ in range(5)]
    word = ''
    mx = 0
    for arr in str_lst:
        if len(arr) >= mx:
            mx = len(arr)
    for j in range(mx):
        for i in range(5):
            if j < len(str_lst[i]):
                word += str_lst[i][j]
    print(f'#{tc}', word)