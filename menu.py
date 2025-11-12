def textlen(text):
    return len(text)

def menu(choices):
    while True:
    
        user_choice = input(f'Choose from {choices}: ').strip()
    
        if user_choice in choices:
            return user_choice

        print(f'{user_choice} is not valid; try again')

if __name__ == '__main__':
    