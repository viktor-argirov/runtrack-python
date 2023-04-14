def triang(a, b, c):
        if a == b == c:
            return "equilateral"
        elif a == b or b == c or c == a:
            if a*a + b*b == c*c or b*b + c*c == a*a or c*c + a*a == b*b:
                return "rectangle et isocele"
            else:
                return "isocele"
        else:
            return "quelconque"
        return "pas un triangle"
print(triang(4,5,5))
print(triang(3,5,6))
print(triang(5,5,5))
print(triang(0,5,10))