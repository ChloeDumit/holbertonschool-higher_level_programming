#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    for name in range(len(dir(hidden_4))):
        if dir(hidden_4)[name][:2] != '__':
            print("{}".format(dir(hidden_4)[name]))
