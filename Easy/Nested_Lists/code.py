if __name__ == '__main__':
    score_dict = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in score_dict:
            score_dict[score].append(name)
        else:
            score_dict[score] = [name]

    new_list = []
    for i in score_dict:
        new_list.append([i, score_dict[i]])

    new_list.sort()

    result = new_list[1][1]

    result.sort()
    print(*result, sep="\n")
