#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    token = dir(hidden_4)
    for name in range(len(token)):
        if token[name][:2] != '__':
            print(token[name])
