def mots_plus_longs(chaine, n):
    mots = chaine.split()
    mots_plus_longs = []
    for mot in mots:
        if len(mot) > n:
            mots_plus_longs.append(mot)
    return mots_plus_longs
chaine = "La peur est le chemin vers le côté obscur la peur mène à la colère la colère mène à la haine la haine mène à la souffrance"
longueur_minimale = 4
resultat = mots_plus_longs(chaine, longueur_minimale)
print(resultat)
