#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        num = fcct(*args)
        return num
    except Exception as err:
        print("Exception:{}".format(err), file=sys.stder)
        return None
