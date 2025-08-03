n = int(input())
a = list(map(int, input().split()))

left = 0
right = n + 1 
ans = 0

# 二分探索
while right - left > 1:
    x = (left + right) // 2

    count = 0
    for val in a:
        if val >= x:
            count += 1

    if count >= x:
        left = x
    else:
        right = x

print(left)