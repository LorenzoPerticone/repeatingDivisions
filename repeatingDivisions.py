#!/usr/bin/env python3

def gcd(n, m):
    if n < m:
        return gcd(m, n)
    if m == 0:
        return n
    return gcd(n % m, m)

def toLowestForm(n, m):
    a = gcd(n, m)
    return n//a, m//a

def normalizeInputString(s):
    if '.' not in s:
        s += '.'
    if '(' not in s:
        s += '(0)'
    return s

def toFraction(s):
    s = normalizeInputString(s)
    
    dot = s.index('.')
    openBrace = s.index('(')
    closedBrace = s.index(')')
    
    integerPart = s[:dot]
    decimalPart = s[dot+1:openBrace]
    repetend = s[openBrace+1:closedBrace]

    t = integerPart + '.' + decimalPart + '(' + repetend + ')'
    if s != t:
        raise ValueError(f'Invalid representation of decimal number {s}')

    num = int(integerPart + decimalPart + repetend) - int(integerPart + decimalPart)
    den = int('9'*len(repetend) + '0'*len(decimalPart))
    return toLowestForm(num, den)

def toString(n, m):
    n, m = toLowestForm(n, m)
    res = ''
    cache = []

    #integer part of the division
    q, r = n // m, n % m
    res = str(q) + '.'
    n = r*10

    #decimal part of the division
    while n != 0:
        q, r = n // m, n % m
        if (q, r) not in cache:
            res += str(q)
            cache.append((q, r))
        else:
            l = len(cache) - cache.index((q, r))
            res = f'{res[:-l]}({res[-l:]})'
            break
        n = r*10

    #w/o this, terminating result will appear w/o a terminating '(0)'
    if n == 0:
        res += '(0)'

    return res

def printString(n, m, res):
    print(f'{n} / {m} = {res}')

def printFraction(s, num, den):
    print(f'{s} = {num} / {den}')

if __name__ == '__main__':
    from sys import argv, exit
    if len(argv) == 2:
        s = argv[1]
        n, m = toFraction(s)
        printFraction(s, n, m)
    elif len(argv) == 3:
        n, m = int(argv[1]), int(argv[2])
        s = toString(n, m)
        printString(n, m, s)
    else:
        name = argv[0]
        print(f'{name} <n> <m>')
        print(f'{name} \'<str>\'')
    exit()
