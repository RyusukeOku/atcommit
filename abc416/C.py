import itertools

N, K, X = map(int, input().split())
S = [input() for _ in range(N)]

all_strings = []
product = itertools.product(S, repeat=K)

for p in product:
    all_strings.append("".join(p))

all_strings.sort()

print(all_strings[X - 1])

