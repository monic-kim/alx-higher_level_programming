#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number of and list of arguments"""
    import sys
    argLen = len(sys.argv) - 1
    if argLen == 0:
        print("0 arguments.")
    elif argLen == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argLen))
    for i in range(argLen):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))

