for moi in range (0,1001):
    if moi > 1 :
        for i in range (2,moi):
            if (moi % i) == 0:
                break 
        else: 
            print(moi)
print(("\nfinito"))                  

print(25%50)