def main():
    a = input('What is the Answer to the Great Question of Life, the Universe, and Everything? ')
    if a == '42' or a.strip().lower() == 'fourty-two' or a.strip().lower() == 'fourty two':
        print('Yes')
    else:
        print('No')

main()