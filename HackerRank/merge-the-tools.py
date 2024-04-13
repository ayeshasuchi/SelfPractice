def merge_the_tools(string, k):
    # your code goes here
    list_t =[]
    for c in range(0,len(string),k):
        list_t.append(string[c:c+k])
    #print(list_t)
    new_list = []
    for i in range(len(list_t)):
        new_list.clear()
        for ch in list_t[i]:
            if ch not in new_list:
                new_list.append(ch)
        print(''.join(new_list))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)