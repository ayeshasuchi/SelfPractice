#It means, the second set should contain all elements of the first set, but the sets must not be equal.

setA = set(map(int,input().split()))
n = int(input().strip())
strict_sup = True
for i in range(n):
    set_others = set(map(int, input().split()))
    if setA.issuperset(set_others) and len(setA) != len(set_others):
        continue
    else:
        strict_sup = False
print(strict_sup)

