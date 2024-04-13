if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    """
     list_arr = list(arr)
    list_runner = [ list_arr[i] for i in range(len(list_arr)) if list_arr[i] < max(list_arr)]
    print(max(list_runner))
    """
    list_arr = list(set(arr))
    list_arr.sort()
    print(list_arr[-2])


