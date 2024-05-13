w = int(input())

i = 1
while True:
    l = 3+i-1
    curr = pow(l, 2) - 2 - l
    if curr == w:
        print(i)
        break
    i += 1