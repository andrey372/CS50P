def main():
    x = input('camelCase: ').strip()
    final_snake = ''
    for i in x:
        if i == i.title():
            final_snake += '_' + i.lower()
        else:
            final_snake += i
    return(final_snake)
print(main())