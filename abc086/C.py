N = int(input())
t = []
x = []
y = []
t.append(0)
x.append(0)
y.append(0)

for i in range(N):
    t_i, x_i, y_i = map(int, input().split())
    t.append(t_i)
    x.append(x_i)
    y.append(y_i)

can_reach = True
for i in range(N):
    t1, x1, y1 = t[i], x[i], y[i]
    t2, x2, y2 = t[i+1], x[i+1], y[i+1]
    dt = t2 - t1
    dist = abs(x2 - x1) + abs(y2 - y1)
    if dt < dist:
        print("No")
        can_reach = False
        break
    if dt % 2 != dist % 2:
        print("No")
        can_reach = False
        break

if can_reach:
    print("Yes")