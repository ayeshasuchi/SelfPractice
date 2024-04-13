n = int(input())
list_tuple = map(int,input().split())
print(hash(tuple(list_tuple)))

'''n = raw_input()
print hash(tuple([int(i) for i in raw_input().split()]))'''

tuple_val = (1, 2)
print("The tuple hash value is : " + str(hash(tuple_val)))