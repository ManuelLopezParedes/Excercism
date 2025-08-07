def value(colors):
    esquema = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
    return int(str(esquema.index(colors[0])) + str(esquema.index(colors[1])))
