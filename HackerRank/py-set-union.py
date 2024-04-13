n = int(input().strip())
set_E = set(map(int,input().split()))
m = int(input().strip())
set_F = set(map(int,input().split()))

number_union = set_E.union(set_F)
print(len(number_union))
