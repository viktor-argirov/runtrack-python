for moi in range(101):
    if moi== 26 or moi == 37 or moi==88:
       continue
    print(moi)

print("\n\tNEXT")  

moinot = (26,37,88)
for moi in range(101):
    if moi not in moinot:
        print(moi)

print("\n\tNEXT") 

for moi in range(0,101):
    if moi == 26 or moi == 37 or moi == 88:
        continue
    print(moi)