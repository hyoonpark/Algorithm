N = int(input())
num_lst = list(map(int, input().split()))
Min = num_lst[0]
Max = num_lst[0]
for num in num_lst:
    if Min > num:
        Min = num
    if num > Max:
        Max = num
print(Min, Max)