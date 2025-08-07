def append(list1, list2):
    list1 += list2
    return list1

def concat(lists):
    lista = []
    for arg in lists:
        lista.extend(arg)
    return lista

def filter(function, list):
    lista = []
    for item in list:
        if function(item):
            lista.append(item)
    return lista

def length(list):
    cuenta = 0
    for i in list:
        cuenta += 1
    return cuenta

def map(function, list):
    lista = []
    for i in list:
        a = function(i)
        lista.append(a)
    return lista

def foldl(function, lista, initial):
    res = initial
    for item in lista:
        res = function(res, item)
    return res


def foldr(function, list, initial):
    res = initial
    for item in reversed(list):
        res = function(res,item)
    return res

def reverse(list):
    lista = []
    for item in range(len(list)-1, -1, -1):
        lista.append(list[item])
    return lista