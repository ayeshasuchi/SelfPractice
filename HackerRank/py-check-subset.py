t = int(input().strip())
for i in range(t):
    na = int(input().strip())
    setA = set(map(int, input().split()))
    nb = int(input().strip())
    setB = set(map(int, input().split()))
    print(setA.issubset(setB))
