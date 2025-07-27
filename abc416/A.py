N, L, R = map(int, input().split())
S = input()
is_possible = True
for i in range(L - 1, R):
    if S[i] == 'x':
        print('No')
        is_possible = False
        break

if is_possible == True:
    print('Yes')