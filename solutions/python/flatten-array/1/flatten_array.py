def flatten(iterable):
    lista =[]
    for item in iterable:
        if isinstance(item,int):
            lista.append(item)
        elif isinstance(item,list):
            lista.extend(flatten(item))
    return lista