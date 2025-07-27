N, Y = map(int, input().split())
x = 0
y = 0
find_solution = False

for x in range(N+1):
    for y in range(N+1 - x):
        if x * 10000 + y * 5000 + (N-x-y) * 1000 == Y:
            z = N - x - y
            if z < 0:
                continue
            find_solution = True
            print(x, y, z)
            exit()

if not find_solution:
    print(-1, -1, -1)