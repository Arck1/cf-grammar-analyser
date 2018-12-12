#!/usr/bin/env python3

G = ["S’→ #S#",
     "S → bbARd",
     "S → abb",
     "R → aR+A",
     "R → b",
     "A →  aAb",
     "A → d"]


class AnalysError(Exception):
    def __init__(self, message):
        self.message = message


def read():
    s = input()
    for c in s:
        yield c


def S1(reader):
    c = next(reader)
    print(G[0])
    if c != '#':
        raise AnalysError('symbol is not #')

    S(reader)
    c = next(reader)
    if c != '#':
        raise AnalysError('symbol is not #')


def S(reader):
    c = next(reader)
    if c == 'b':
        print(G[1])
        c = next(reader)
        if c == 'b':
            A(reader)
            R(reader)
            c = next(reader)

            if c != 'd':
                raise AnalysError(f"{c} is not d")
            return
        else:
            raise AnalysError(f"{c} is not b")
    elif c == 'a':
        print(G[2])
        for i in range(2):
            c = next(reader)
            if c != 'b':
                raise AnalysError(f"{c} is not a")
    else:
        raise AnalysError(f"S → rules don't start with {c}")


def R(reader):
    c = next(reader)
    if c == 'b':
        print(G[4])
        return
    elif c == 'a':
        print(G[3])
        R(reader)
        c = next(reader)
        if c != '+':
            raise AnalysError(f"{c} is not +")
        A(reader)
    else:
        raise AnalysError(f'{c} is not in R rules')


def A(reader):
    c = next(reader)
    if c == 'd':
        print(G[6])
        return
    elif c == 'a':
        print(G[5])
        A(reader)
        c = next(reader)
        if c != "b":
            raise AnalysError(f"{c} is not b")
    else:
        raise AnalysError(f"{c} is not in A rules")


def main():
    reader = read()

    S1(reader)
    print("ok")


if __name__ == '__main__':
    main()
