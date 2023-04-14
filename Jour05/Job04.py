text ="Jules Cesar general et stratege romain"
alphabet="abcdefghijklmnopqrstuvwxyz"
coded_text=""
print("\n" + text)
#print ("\n" + alphabet)
#print (text [e])
#print (text [1])
for i in range(len(text)) :
    if text[i].casefold()==" ":
        coded_text+=" "
    for j in range(len(alphabet)):
     if text[i].casefold()==alphabet [j]:
      coded_text += alphabet [j+2]
print(coded_text)
