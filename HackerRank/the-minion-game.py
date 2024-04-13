def minion_game(string):
    # your code goes here
    vowel_str ="AEIOU"
    Kevin_score =0
    Stuart_score =0
    len_str = len(string)

    for i in range(len_str):
        if string[i] in vowel_str:
            Kevin_score += len_str-i
        else:
            Stuart_score += len_str - i

    if Kevin_score > Stuart_score:
        print(f"Kevin {Kevin_score}")
    elif Stuart_score > Kevin_score:
        print(f"Stuart {Stuart_score}")
    else:
        print(f"Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)