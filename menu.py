def textlen(text):
    return len(text)

def menu(choices):
    while True:
    
        user_choice = input(f'Choose from {choices}: ').strip()
    
        if user_choice in choices:
            return user_choice

        print(f'{user_choice} is not valid; try again')

if __name__ == '__main__':
    # this block will not run when menu.py is imported
    # this block *will* run when menu.py is executed from the command line as a standalone program

    user_choice = menu(['a', 'b', 'c'])
    print(f'You chose {user_choice}')
    