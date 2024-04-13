if __name__ == '__main__':
    list_second = []
    list_num = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list_second.append([name, score])
        list_num.append(score)
    list_sorted_num = list(set(list_num))
    list_sorted_num.sort()
    second_max = list_sorted_num[1]
    list_name = [list_second[head][0] for head in range(len(list_second)) if list_second[head][1] == second_max]
    list_name.sort()
    print(*list_name, sep='\n')














