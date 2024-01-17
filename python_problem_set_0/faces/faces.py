def main():
    message = input()
    convert(message)

def convert(message):
    output = ''
    idx = 0
    while idx != len(message):
        if message[idx] == ':' and message[idx+1] == '(':
            output += "😐"
            idx += 2
        elif message[idx] == ':' and message[idx+1] == ')':
            output += "🙂"
            idx += 2
        else:
            output += message[idx]
            idx += 1
    print(output)


main()