if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    items = list(arr)

    max = -99
    runner_up = -100

    for i in items:
        if (i > max):
            max = i

    for i in items:
        if (i > runner_up and i < max):
            runner_up = i

    print(runner_up)
