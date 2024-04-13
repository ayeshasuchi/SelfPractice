if __name__ == '__main__':
    N = int(input())
    list_arr=[]
    for i in range(N):
        input_str = str(input())
        #print(input_str)
        list_str = input_str.split()
        #print(list_str)
        if 'insert' in input_str:
            list_arr.insert(int(list_str[1]),int(list_str[2]))
        elif 'print' in input_str:
            print(list_arr)
        elif 'remove' in input_str:
            list_arr.remove(int(list_str[1]))
        elif 'append' in input_str:
            list_arr.append(int(list_str[1]))
        elif 'sort' in input_str:
            list_arr.sort()
        elif 'pop' in input_str:
            list_arr.pop()
        elif 'reverse' in input_str:
            list_arr.reverse()

    #print(list_arr)
"""
insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
"""