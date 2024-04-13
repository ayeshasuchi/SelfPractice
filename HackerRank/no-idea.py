n, m = list(map(int, input().split()))
list_arr = list(map(int, input().split()))
set_A = set(map(int, input().split()))
set_B = set(map(int, input().split()))
happiness =0
for element in list_arr:
    if element in set_A and element not in set_B:
        happiness+=1
    if element in set_B:
            happiness -= 1
print(happiness)
