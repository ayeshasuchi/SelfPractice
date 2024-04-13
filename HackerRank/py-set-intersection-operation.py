n = int(input().strip())
set_E = set(map(int,input().split()))
m = int(input().strip())
set_F = set(map(int,input().split()))

number_intersection = set_E.intersection(set_F)
print(len(number_intersection))
