#Un gardien de phare va aux toilettes cinq fois par jour. Or les WC sont au
#rez-de-chaussée...
#Écrire une fonction qui reçoit en paramètres, le nombre de marches du phare et la
#hauteur de chaque marche (en cm), cette fonction doit calculer combien de mètre le
#gardien effectué par semaine pour aller aux toilettes. La sortie du code doit être :
#Pour x marches de y cm, le gardien parcours z.zz m par semaine.
def distance_toilettes(marches, hauteur):
    distance_marche = hauteur / 100
   
    distance_double_marche = 2 * distance_marche

    distance_totale = marches * distance_marche
  
    distance_totale += (marches - 1) * distance_double_marche
  
    distance_semaine = 2 * distance_totale * 2 * 7
    
    resultat = "Pour {} marches de {} cm, le gardien parcours {:.2f} m par semaine.".format(marches, hauteur, distance_semaine)
   
    return resultat
marches = 10
hauteur = 15
resultat = distance_toilettes(marches, hauteur)
print(resultat)

