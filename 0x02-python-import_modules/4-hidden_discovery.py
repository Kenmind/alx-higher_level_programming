#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    funcs = dir(hedden_4)
    for i in funcs:
        if not i.startswith("__"):

            print("{:s}".format(i))
