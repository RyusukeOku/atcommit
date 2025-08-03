from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

freq = defaultdict(int)
count = 0

for j in range(n):
    count += freq[j - a[j]]
    
    freq[j + a[j]] += 1
    
print(count)