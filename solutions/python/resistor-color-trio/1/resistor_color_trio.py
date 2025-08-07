def label(colors):
    esquema = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
    r = ((esquema.index(colors[0]) * 10) + esquema.index(colors[1])) * (10 ** esquema.index(colors[2]))
    if r < 1000:
        return f"{r} ohms"
    elif r < 1000000:
        return f"{r//1000} kiloohms"
    elif r < 1000000000:
        return f"{r//1000000} megaohms"
    else:
        return f"{r//1000000000} gigaohms"
