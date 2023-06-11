#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    _lista = list(tuple_a)
    if len(_lista) < 2:
        for i in range(len(_lista), 2):
            _lista.append(0)

    list_b = list(tuple_b)
    if len(list_b) < 2:
        for i in range(len(list_b), 2):
            list_b.append(0)
    new = [_lista[0] + list_b[0], _lista[1] + list_b[1]]
    tuple_new = tuple(new)
    return tuple_new
