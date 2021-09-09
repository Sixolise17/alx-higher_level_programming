#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    dir = dir()
    for i in range(0, len(dir)):
        if dir[i][0:2] != "__":
            print("{}".format(dir[i]))
