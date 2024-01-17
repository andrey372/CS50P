def playback(message):
    output = ''
    for i in message:
        if i == ' ':
            output += '...'
        else:
            output += i
    print(output)

message = input('Type your message: ')
playback(message)
