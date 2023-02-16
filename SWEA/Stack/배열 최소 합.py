def minSum(i, num_sum):
    global sum_min

    if num_sum >= sum_min:   # 현재 합이 최소합보다 크거나 같으면 종료
        return
    if i == N:  # i가 N이랑 같아지면
        if num_sum < sum_min:
            sum_min = num_sum
        return

    for j in range(N):
        if visited[j]:
            continue
        visited[j] = 1  # 방문표시
        minSum(i+1, num_sum+num_lst[i][j])  # 다음 행에서 함수 호출, 그리고 그 값을 더해준것을 같이 보냄
        visited[j] = 0  # 재귀 함수 끝나면 방문표시 지워준다



for t in range(1, int(input())+1):
    N = int(input())
    num_lst = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N  # 사용한 열
    sum_min = 100   # 문제에서 N의 최댓값이 10이고 0~9까지의 정수가 주어지므로
    minSum(0, 0)
    print(f'#{t}', sum_min)