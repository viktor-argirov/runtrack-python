for moi in range(1, 101):
    if moi % 3 == 0 and moi % 5 == 0:
        print("FizzBuzz",moi)
    elif moi % 3 == 0:
        print("Fizz",moi)
    elif moi % 5 == 0:
        print("Buzz",moi)
    else:
        print(moi)
