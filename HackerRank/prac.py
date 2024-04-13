'''if __name__ == '__main__':
    n = int(input())
    tn = input().split()
    print(hash(tuple(int(i) for i in tn)))'''

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9, 66, 11, 55}
setB = {35, 7, 22, 58, 62}
setA.symmetric_difference_update(setB)
#print(setA)


setA = {1, 3, 4}
setB = {1,3}
print(setA.issuperset(setB))
