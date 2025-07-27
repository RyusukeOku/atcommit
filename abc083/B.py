N, A, B = map(int, input().split())

total = 0
for i in range(N+1):
    digits = [int(digit) for digit in str(i)]
    if sum(digits) >= A and sum(digits) <= B:
        total += i

print(total)