Liste = []
ListeResultat = []

def ech(Liste):
    """ Fonction prenant une liste
    """
    ListeResultat.append(Liste[1])
    ListeResultat.append(Liste[0])
    i = 2
    while i < len(Liste):
        ListeResultat.append(Liste[i])
        i += 1
    return(ListeResultat)

