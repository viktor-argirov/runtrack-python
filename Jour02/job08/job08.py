def alien(type,saison):
    if type == "fruits" and saison == "hiver": 
        return ("orange","mandarin","kiwi")
    elif type == "fruits" and saison == "ete":
        return ("poire","fraise","cassis")
    elif type == "legumes" and saison == "hiver":
        return ("carrote","topinambour","endive")
    elif type == "legumes" and saison == "ete":
        return("artichaut","aubergine","navet") 
print(alien("fruits","ete"))
print(alien("legumes","hiver"))
print(alien("fruits","hiver"))
print(alien("legumes","ete"))