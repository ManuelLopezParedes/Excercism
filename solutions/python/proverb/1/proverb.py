def proverb(*objeto,qualifier=None):
    if not objeto:
        return []
    
    res = []
    
    for i in range(len(objeto) -1):
        res.append(f"For want of a {objeto[i]} the {objeto[i+1]} was lost.")

    if qualifier:
        res.append(f"And all for the want of a {qualifier} {objeto[0]}.")
    else:
        res.append(f"And all for the want of a {objeto[0]}.")
    return res