n = int(input().strip())
set_E = set(map(int,input().split()))
m = int(input().strip())
set_F = set(map(int,input().split()))

number_difference = set_E.difference(set_F)
print(len(number_difference))
