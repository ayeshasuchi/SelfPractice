# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
list_N = list(map(int, input().split()))

M = int(input())
list_M = list(map(int, input().split()))

final_list=[]
set_N = set(list_N)
set_M = set(list_M)

setdiff_N_M = set_N.difference(set_M)
setdiff_M_N = set_M.difference(set_N)

final_list.extend(setdiff_N_M,)
final_list.extend(setdiff_M_N)
final_list.sort()
for i in final_list:
    print(i)