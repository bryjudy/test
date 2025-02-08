def check_discriminant(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        return "Discriminant is positive"
    elif discriminant < 0:
        return "Discriminant is negative"
    else:
        return "Discriminant is zero"
