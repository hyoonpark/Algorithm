for tc in range(1, 11):
    N = int(input())
    mag = [list(map(int, input().split())) for _ in range(100)]
    mag_t = list(map(list, zip(*mag)))
    cnt = 0
    
    print(f'#{tc}', cnt)