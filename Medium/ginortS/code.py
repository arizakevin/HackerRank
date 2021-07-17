# Enter your code here. Read input from STDIN. Print output to STDOUT
def ginortS(s):
    code = 0
    if s.isupper():
        code = 10 ** 3
    elif s.isdigit():
        code = 10 ** 6
        if ord(s) % 2 == 0:
            code = 10 ** 9
    return code + ord(s)


if __name__ == "__main__":
    print(*sorted(input(), key=lambda s: ginortS(s)), sep='')
