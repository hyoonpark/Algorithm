from itertools import combinations

N, K = map(int, input().split())
all_combinations = set(range(1, N+1))
poisonous_combination = set(map(int, input().split()))

for _ in range(K):
    for i in range(1, len(poisonous_combination) + 1):
        for subset in combinations(poisonous_combination, i):
            all_combinations.discard(subset)

print(len(all_combinations))