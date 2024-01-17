def main():
    m = input()
    if not m:
        e()
    else:
        e(m)

def e(m = 1):
    m = int(m)
    c = 300000000
    print(m * (c * c))

main()