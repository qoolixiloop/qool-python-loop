#!/usr/bin/env python
# -*- coding: utf-8 -*-

def clean_num(num):
    numstr = str(num)
    if (numstr.startswith('0b')
            or numstr.startswith('0x')
            or numstr.startswith('0o')):
        numstr = numstr[2:]
    elif numstr.startswith('0'):
        numstr = numstr[1:]
    numstr = numstr.upper()
    return numstr

def isvalid(numstr, origin):
    if origin.startswith("D"): 
        if numstr.isdigit():
            return True
        else:
            return False
    elif origin.startswith("H"):
        for c in numstr:
            if c in "0123456789ABCDEF":
                continue
            else:
                return False
        return True
    elif origin.startswith("B"):
        for c in numstr:
            if c in "01":
                continue
            else:
                return False
        return True
    elif origin.startswith("O"):
        for c in numstr:
            if c in "01234567":
                continue
            else:
                return False
        return True
    else:
        return False

def from_hex(numstr):
    hexd = {'A':10,
            'B':11,
            'C':12,
            'D':13,
            'E':14,
            'F':15 }
    result = 0
    for i in xrange(len(numstr)):
        if numstr[-(i+1)] in hexd:
            result += hexd[numstr[-(i+1)]] * (16 ** i)
        else:
            result += int(numstr[-(i+1)]) * (16 ** i)
    return result

def from_oct(numstr):
    result = 0
    for i in xrange(len(numstr)):
        result += int(numstr[-(i+1)]) * (8 ** i)
    return result

def from_bin(numstr):
    result = 0
    for i in xrange(len(numstr)):
        result += int(numstr[-(i+1)]) * (2 ** i)
    return result

def convert(origin, target, num):

    numstr = clean_num(num)

    if not isvalid(numstr, origin):
        return "Error: not a valid {} number".format(origin)

    if origin != "Decimal":
        if origin == "Hexadecimal":
            intermediate = from_hex(numstr)
        elif origin == "Octal":
            intermediate = from_oct(numstr)
        else:
            intermediate = from_bin(numstr)
    else:
        intermediate = int(numstr)

    if target == "Decimal":
        return str(intermediate)
    elif target == "Binary":
        return bin(intermediate)
    elif target == "Hexadecimal":
        return hex(intermediate)
    else:
        return oct(intermediate)

if __name__ == "__main__":
    convert("Decimal", "Binary", "145")
