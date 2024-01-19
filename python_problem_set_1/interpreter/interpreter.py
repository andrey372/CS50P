def main():

    x, y, z = input('Expression: ').strip().split()
    x = float(x)
    z = float(z)

    if y == '+':
        return round(x + z, 1)
    elif y == '-':
        return round(x - z,1)
    elif y == '*':
        return round(x * z, 1)
    elif y == '/':
        return round(x / z, 1)

print(main())