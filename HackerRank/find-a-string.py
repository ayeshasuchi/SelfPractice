def count_substring(string, sub_string):
    len_sub = len(sub_string)
    count =0
    for subs in range(len(string)):
        #print (string[subs:subs+len_sub])
        if string[subs:subs+len_sub] == sub_string:
            count+=1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)