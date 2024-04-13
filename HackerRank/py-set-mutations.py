# Enter your code here. Read input from STDIN. Print output to STDOUT
na = int(input().strip())
set_A = set(map(int, input().split()))
n = int(input().strip())
for i in range(n):
    operation, m = list(map(str, input().split()))
    set_B = set(map(int, input().split()))
    # print(operation)
    # print(set_B)
    if 'intersection_update' in operation:
        set_A.intersection_update(set_B)
        # print(set_A)

    elif 'symmetric_difference_update' in operation:
        set_A.symmetric_difference_update(set_B)
        # print(set_A)
    elif 'difference_update' in operation:
        # print(set_A)
        set_A.difference_update(set_B)
        # print(set_A)
    elif 'update' in operation:
        set_A.update(set_B)
        # print(set_A)

print(sum(set_A))
