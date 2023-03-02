'''
0. 문자열로 받고, 같은 길이의 리스트를 하나 만들어준다.
1. 각각의 인덱스에 있는 요소와 같은지 확인하고 다르다면 그 이후 요소들을 다 바꿔준다.
2. 한번 바꿔줄때마다 cnt +1 해준다.
3. 모든 요소를 비교했다면 while문을 벗어나고, 정답을 출력한다.
'''

for tc in range(1, int(input())+1):
    m = list(input())
    n = ['0' for _ in range(len(m))]
    cnt = 0
    while True:
        for i in range(len(m)):
            if m[i] != n[i]:
                for x in range(i, len(m)):
                    n[x] = m[i]
                cnt += 1
        break
    print(f'#{tc}', cnt)