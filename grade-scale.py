g = input()
n = int(input())
m = list(map(int, input().split()))

r = {
    'A+': 90,
    'A': 80,
    'A-': 75,
    'B+': 70,
    'B': 65,
    'C+': 60,
    'C': 50,
    'D': 40,
    'E': 30,
    'F': 0
}

count = 0
for i in m:
    if i >= r[g]:
        count += 1

print(count)