def recite(start_verse, end_verse):
    verso_i = start_verse - 1
    verso_f = end_verse - 1
    lista = []
    texto = ""

    this = ["This is the house that Jack built.",
             "This is the malt ", 
             "This is the rat ",
             "This is the cat ",
             "This is the dog ",
             "This is the cow with the crumpled horn ",
             "This is the maiden all forlorn ",
             "This is the man all tattered and torn ",
             "This is the priest all shaven and shorn ",
             "This is the rooster that crowed in the morn ",
             "This is the farmer sowing his corn ",
             "This is the horse and the hound and the horn "
            ]

    that =["that lay in the house that Jack built.",
            "that ate the malt ",
            "that killed the rat ",
            "that worried the cat ",
            "that tossed the dog ",
            "that milked the cow with the crumpled horn ",
            "that kissed the maiden all forlorn ",
            "that married the man all tattered and torn ",
            "that woke the priest all shaven and shorn ",
            "that kept the rooster that crowed in the morn ",
            "that belonged to the farmer sowing his corn "
            ]
    
    while verso_i <= verso_f:
        for j in range(verso_i,-1,-1):
            if j == verso_i:
                texto += this[j]
            else:
                texto += that[j]
            
        lista.append(texto)
        texto = ""
        verso_i += 1
    
    return lista