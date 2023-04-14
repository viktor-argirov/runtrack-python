L=[8,24,48,2,16]
x=len(L)
multi= 0 
for i in range (x):
       if L[i] % 3 == 0 :
        multi=multi+1
        print(multi)
