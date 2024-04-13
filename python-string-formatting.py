def print_formatted(number):
    len_bin = len(bin(number)[2:])
    for i in range(1, number + 1):
        print(str(i).rjust(len_bin), '', (oct(i)[2:]).rjust(len_bin), '', ((hex(i)[2:]).upper()).rjust(len_bin), '', str(bin(i)[2:]).rjust(len_bin))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
