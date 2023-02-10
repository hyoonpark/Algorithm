GNS = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for t in range(1, int(input()) + 1):
    tc = input().split()
    words = input().split()
    number = [0] * 10

    for word in words:
        for idx, element in enumerate(GNS):
            if element == word:
                number[idx] += 1
                break

    print(tc[0])

    for i in range(10):
        print((GNS[i] + ' ') * number[i], end=' ')
    print()