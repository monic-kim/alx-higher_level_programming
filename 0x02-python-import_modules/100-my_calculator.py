#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    argv = sys.argv[1:]
    argv_count = len(argv)
    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if argv_count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b")
        exit(1)
    elif sys.argv[2] not in list(ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        result = ops[sys.argv[2]](a, b)
        print("{} {} {} = {}".format(a, sys.argv[2], b, result))
