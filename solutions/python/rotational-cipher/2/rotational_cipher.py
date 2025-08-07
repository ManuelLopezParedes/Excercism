def rotate(text, key):
    alf = "abcdefghijklmnopqrstuvwxyz"
    ALF = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    for element in text:
        if element in alf:
            index = alf.index(element)
            sum = index + key
            if sum >= len(alf):
                resta = sum - len(alf)
                sum = resta
            res += alf[sum]
        elif element in ALF:
            index = ALF.index(element)
            sum = index + key
            if sum >= len(ALF):
                resta = sum - len(ALF)
                sum = resta
            res += ALF[sum]
        else:
            res += element
    return res
