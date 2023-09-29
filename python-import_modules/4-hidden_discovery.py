#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    i = dir(hidden_4)
    for i in names:
        if i[:2] != "__":
            print(i)
