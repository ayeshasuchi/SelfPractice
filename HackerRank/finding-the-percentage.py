if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    list_query = student_marks[query_name]
    average = sum(list_query)/len(list_query)
    print(f"{average:.2f}")
