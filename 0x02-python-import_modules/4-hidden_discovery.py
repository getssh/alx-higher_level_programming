#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4


nw = dir(hidden_4)
i = 0
while (i < len(nw)):
    if (nw[i][0] != "_"):
        print(nw[i])
    i += 1
