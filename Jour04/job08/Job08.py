L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
sum=0 
for value in L:
    if value % 2 ==0:
        sum+=value
print(sum)

#pour avoir sum
L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
sum = sum(L)
print(sum)
