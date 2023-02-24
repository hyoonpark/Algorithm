arr = [['D', 'A', 'T', 'A', 'W'], ['B', 'B', 'Q', 'K']]
N = int(input())
if N%2:
    arr[0].sort()
    print(''.join(arr[0]))
    print(''.join(arr[1]))
else:
    arr[1].sort()
    print(''.join(arr[0]))
    print(''.join(arr[1]))