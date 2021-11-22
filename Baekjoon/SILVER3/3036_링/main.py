import math

n = int(input())
circles = list(map(int, input().split()))
ring1 = circles[0]
for r in range(1, len(circles)):
    ring = circles[r]
    gcd = math.gcd(ring1, ring)
    print("{}/{}".format(ring1//gcd, ring//gcd))