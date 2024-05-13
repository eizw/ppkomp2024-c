d = [*input()]
d.sort()

b, s = '', ''
if len(d) < 2 or int(''.join(d)) == 0:
    b, s = int(d), int(d)
else:
    # small
    temp = d.copy()
    for i in temp:
        if i != '0':
            s += i
            temp.remove(i)
            break
    s += ''.join([i for i in temp])

    
    # big
    temp = d.copy()
    temp.sort(reverse=True)
    for i in temp:
        if i != '0':
            b += i
            temp.remove(i)
            break
    b += ''.join([i for i in temp])
    s, b = int(s), int(b)

print(s, b)
print(s + b)