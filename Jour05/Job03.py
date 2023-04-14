def x(n):
    for i in range(n+1):
        for j in range(n+1):
            if i == j:
                print("/",end="")
            else:
                print("#",end="")
        print()
x(10)



y=10
u=5
print("Rectangle")

for i in range(y):
    print("|"+"-"*y + "|")
