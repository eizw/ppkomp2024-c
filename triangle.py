import math

ab = int(input())
bc = ab / 2
ac = math.ceil(math.sqrt(pow(ab, 2) + pow(bc ,2)))

area = ab * bc // 2
perimeter = ab + bc + ac

print(int(area), int(perimeter))