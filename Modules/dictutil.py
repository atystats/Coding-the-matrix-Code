# Copyright 2013 Philip N. Klein
def dict2list(dct, keylist): return [dct[x] for x in keylist]

def list2dict(L, keylist): return {keylist[x]:L[x] for x in range(len(keylist))}

def listrange2dict(L): return {x:L[x] for x in range(len(L))}
