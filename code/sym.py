class Sym:
    def __init__(self, c, s):
        self.n = 0
        self.at = c or True
        self.name = s or True
        self._has = dict()
        
    
    def add(v):
        if (v != "?"):
            self.n = self.n + 1
            if v in self._has:
                self._has[v] = 1 + self._has[v]
            else: self._has[v] = 1

def mid(self,col,most,mode):
    most=-1
    for k,v in self._has.items():
        if v > most:
            mode=k
            most=v
    return mode

def div(self,e,fun):
    def fun(p):
        return p*math.log(p,2)
    e=0
    for _,n in self._has.items():
        if n>0:
            e=e-fun(n/self.n)
    return e