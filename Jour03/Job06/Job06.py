s = "abcdefghijklmnopqrstuvwxyz" * 10
n = len(s)
rows = 0
while rows*(rows+1)//2 <= n:
    rows += 1
rows -= 1  # Adjust for overshooting the number of characters
k = 0
for i in range(rows):
    spaces = " " * (rows-i-1)
    print(spaces + " ".join(s[k:k+i+1]))
    k += i+1
print(" " * (rows-1) + s[k:])


("\n\tNEXT")


def textinpyramide(text):
    name = 1 
    while len (text)>name:
        print(text[0:name:])
        text = text [name::]
        name +=1 
text = "abcdefghijklmnopqrstuvwxyz"* 10
textinpyramide(text)