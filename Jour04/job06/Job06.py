def swap_first_last(y):
    if len(y)>1:
        y[0],y[-1] = y[-1],y[0]
        return y
y=[1,2,3,4,5]
print(swap_first_last(y))
