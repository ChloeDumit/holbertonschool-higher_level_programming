#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    for str in range(len(sys.argv)):
        if len(sys.argv) != 4:
            print("Usage: ./100-my_calculator.py <a> <operator> <b>")
            exit(1)
        else:
            a = sys.argv[1]
            b = sys.argv[3]
        if sys.argv[2] == '+':
            print("{:d} + {:d} = {:d}".format(a, b, add(a,b)))
        elif sys.argv[2] == '-':
            print("{:d} - {:d} = {:d}".format(a, b, sub(a,b)))
        elif sys.argv[2] == '*':
            print("{:d} * {:d} = {:d}".format(a, b, mul(a,b)))
        elif sys.argv[2] == '/':
            print("{:d} / {:d} = {:d}".format(a, b, div(a,b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        exit(0)