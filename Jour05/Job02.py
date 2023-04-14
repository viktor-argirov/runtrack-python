#Écrire un programme qui affiche dans le terminal un rectangle avec des ‘-’ et des ‘|’ en
#fonction des paramètres d’entrées, (width, height), par exemple :
#draw_rectangle(10, 3)

def rectangle(width, height):
    for i in range(height):
        if i == 0 or i == height-1:
            print("-" * width)
        else:
            print("|" + " "*(width-2) + "|")
rectangle(10,3)
#
y=10
u=5
print("Rectangle")

for i in range(y):
    print("|"+"-"*y + "|")