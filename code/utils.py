# Handle settings
import math
import re

def is_num(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def func(s1):
    if s1 == "true":
        return True
    elif s1 == "false":
        return False
    return s1

def coerce(s):
    if is_num(s):
        return float(s)
    else:
        return func(s) or None

def cli():
    pass


# Lists 
def copy(t):
    """Deep Copy"""
    if(type(t) == 'dict'):
        u = {}
        for k,v in t.items():
            u[k] = v
        return u

    # assume t is a list 
    u = []
    for x in t:
        u.append(x)
    return u
    
        

def per(t, p=0.5):
    """Return the pth thing from the sorted list t"""
    p = math.floor(p*len(t)+0.5)
    p = p - 1
    return t[max(0, min(len(t)-1, p))]

def push(t, x):
    kys = sorted(t.keys())
    pos = len(kys)
    t[pos] = x
    return x

def csv(fname, fun):
    """Call fun on each row. Row cells are divided in the.seperator"""
    sep = "," #edit this line
    src = open(fname)
    while True:
        s = src.readline()
        if not s:
            return src.close()
        else:
            t={}
            for s1 in s.split(sep):
                t[1+len(t)] = coerce(s1)
            fun(t) #findout fun
            
    
# Strings
def o(t):
    if type(t) != dict:
        return str(t)
    def show(k, v):
        match_str= re.compile("^_")
        if not re.findall(match_str, str(k)):
            v = o(v)
            return len(t)==0 and "{}".format(k,v) or str(v)
    u = dict()
    for k, v in t.items():
        u[1+len(u)] = show(k, v)
    if len(t)==0:
        sorted(u)
    return u

def oo(t):
    print(o(t))
    return t


# Miscs

def rouges():
    pass


# Maths
def rnd(x, places=2):
    mult = 10 ** places
    return math.floor(x * mult + 0.5) // mult


if __name__ == "__main__":
    # t = {
    #     "h": 10,
    #     "z": 27,
    #     "abc": {"1": 10}
    # }
    
    # t = [1,2,3,4,5]
    
    # print(t)
    # u = copy(t)
    # print(u)
    # print(t == u)
    
    t = {0: 1, 1: 2,2: 3, 3: 4,4: 5,5: 6}
    
    print(per(t,-2))
    
    print(t)
    
    push(t, 20)
    print(t)
    
    