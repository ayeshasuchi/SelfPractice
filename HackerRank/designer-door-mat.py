n, m = list(map(int, input().split()))
middle_pos = (n // 2)+1

sa = 'WELCOME'
sb = '.|.'

inc_size = 1;

for i in range(1, n + 1):
    if i == middle_pos:
        print(sa.center(m, '-'))
    elif i < middle_pos:
        print((sb * inc_size).center(m, '-'))
        inc_size += 2
    elif i > middle_pos:
        inc_size -= 2
        print((sb * inc_size).center(m, '-'))
