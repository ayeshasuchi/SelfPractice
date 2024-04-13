def average(array):
    # your code goes here
    arr_set = set(array)
    avg_set = sum(arr_set)/len(arr_set)
    string_out = f"{avg_set:.3f}"
    return string_out

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)