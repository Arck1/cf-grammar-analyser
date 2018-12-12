G = ["S’→ #S#",
     "S → bbARd",
     "S → abb",
     "R → aR+A",
     "R → b",
     "A →  aAb",
     "A → d"]

reader = None
c = None


class AnalysError(Exception):
    def __init__(self, message):
        self.message = message


def read():
    s = input()
    for c in s:
        yield c


def S1():
    global c
    global reader
    print(G[0])
    if c != '#':
        raise AnalysError('symbol is not #')
    c = next(reader)
    S()
    c = next(reader)
    if c != '#':
        raise AnalysError('symbol is not #')


def S():
    global reader
    global c
    if c == 'b':
        print(G[1])
        c = next(reader)
        if c == 'b':
            c = next(reader)
            A()
            c = next(reader)
            R()
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


def R():
    global reader
    global c
    if c == 'b':
        print(G[4])
        return
    elif c == 'a':
        print(G[3])
        c = next(reader)
        R()
        c = next(reader)
        if c != '+':
            raise AnalysError(f"{c} is not +")
        c = next(reader)
        A()
    else:
        raise AnalysError(f'{c} is not in R rules')


def A():
    global reader
    global c

    if c == 'd':
        print(G[6])
        return
    elif c == 'a':
        print(G[5])
        c = next(reader)
        A()
        c = next(reader)
        if c != "b":
            raise AnalysError(f"{c} is not b")
    else:
        raise AnalysError(f"{c} is not in A rules")


def main():
    global c
    global reader
    reader = read()
    c = reader.__next__()
    S1()
    print("ok")


if __name__ == '__main__':
    main()
