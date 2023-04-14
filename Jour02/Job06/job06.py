def alien(nombre):
    if nombre > 0:
       return "positif"
    elif nombre < 0:
         return "negatif" 
    else : print("rien")
print(alien(5))     
print(alien(50))
print(alien(-80))
print(alien(-1))
print(alien(0))