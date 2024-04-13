k = int(input().strip())
list_grp = list(map(int, input().split()))
set_grp = set(list_grp)
set_grp.issubset()
for element in set_grp:
    list_grp.remove(element)
    if element not in list_grp:
        print(element)
        break



'''
n = int(raw_input());
dic = {} 
for x in raw_input().split():
  dic[x] = dic.get(x,0) + 1
for key in dic:
  if dic[key] != n: 
    print key
    break



result = [x for x in list_grp if list_grp.count(x) == 1]
for element in result:
    print(element)

for element in set_grp:
    if list_grp.count(element) == 1:
        print(element)
        break'''
