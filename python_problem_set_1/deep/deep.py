# In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.

def main():
    a = input('What is the Answer to the Great Question of Life, the Universe, and Everything? ')
    if a == '42' or a.strip().lower() == 'fourty-two' or a.strip().lower() == 'fourty two':
        print('Yes')
    else:
        print('No')

main()