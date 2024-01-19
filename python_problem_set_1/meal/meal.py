def main():
    x = input('What time is it? ').strip()

    def convert(time):
        hours, minutes = time.split(':')
        hours = int(hours)
        minutes = int(minutes)

        if hours >= 7 and hours < 8:
            if minutes >= 0 and minutes <= 60:
                return 'breakfast time'
        elif hours == 8:
            if minutes == 0:
                return 'breakfast time'

        elif hours >= 12 and hours < 13:
            if minutes >= 0 and minutes <= 60:
                return 'lunch time'
        elif hours == 13:
            if minutes == 0:
                return 'lunch time'
            
        elif hours >= 18 and hours < 19:
            if minutes >= 0 and minutes <= 60:
                return 'dinner time'
        elif hours == 19:
            if minutes == 0:
                return 'dinner time'
            
    if convert(x) != None:
        print(convert(x))

main()