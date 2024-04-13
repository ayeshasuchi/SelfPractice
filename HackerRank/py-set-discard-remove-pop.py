n = int(input())
s = set(map(int, input().split()))
m = int(input())

for i in range(m):
    input_str = list(map(str,input().split()))

    if 'remove' in input_str:
        s.remove(int(input_str[1]))
    elif 'discard' in input_str:
        s.discard(int(input_str[1]))
    elif 'pop' in input_str:
        s.pop()

print(sum(s))