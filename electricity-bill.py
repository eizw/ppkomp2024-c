p, c = list(map(int, input().split()))
a = c - p

rate = [0.218, 0.334, 0.516, 0.546, 0.571]
w = [200, 100, 300, 300, 0]
cost = 0

for i in range(len(rate)):
    temp = a
    a -= w[i]
    if a <= 0 or w[i] == 0:
        cost += temp * rate[i]
        break
    else:
        cost += w[i] * rate[i]

print(f'{c-p}kWh')
print('RM%.02f' % cost)