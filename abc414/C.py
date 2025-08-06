a = int(input())
n = int(input())
ans = 0

for i in range(n):
    if i % 2 == 0:
        i = str(i + 1)
        i_half = i[:len(i)//2]
        i_half_rev = i_half[::-1]
        i = i_half + i_half_rev
        print(i)
    else:
        i = str(i + 1)
        i_half = i[:(len(i)+1)//2]
        i_half_rev = i_half[::-1]
        i = i_half + i_half_rev
        print(i)