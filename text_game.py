def run():

    print('Welcome to my first text adventure hope you enjoy! ')

    name = input('What\'s your name? ').title()
    items = []

    print(f'Hi! {name} you woke up a little fuzzy and you are in a room!')

    first = input('What do you want to do? investigate the room or try to go out (investigate/out)')

    if first == 'investigate' or 'i':
        print('You found interesting things')
        investiagate_things = input('a desk, a table and a bed which do you want to investigate? (desk/table/bed)').lower()
    
        if investiagate_things == 'desk' or 'd':
            print('You found sunglasses')
            desicion = input('Do you want to take the glasses? (yes/no)').lower()
            if desicion == 'yes' or 'y':
                items.append('glasses')
                print(f'now you have a new item {items}')
                final_2 = input('You want to go out of the room? (yes/no)').lower()
           
                if final_2 == 'yes' or 'y' and 'glasses' in items:
                    print('There is a giant light and a door')
                    desicion_2 = input('What do you want to do? (run/stay)').lower()
                    if desicion_2 == 'run' or 'r':
                        print('You scaped from that room you\'re finally free. Congratulations')
                    else:
                        print('You stayed for too long and died from the light :(. Loser.')    
            else:
                print('Then you went to sleep again')
    
        elif investiagate_things == 'table':
            print('There\'s nothing interesting on the table')
        elif investiagate_things == 'bed':
            print('What a nice pillow we have here')
        else:
            print('You hurt yourself and died')

    elif first == 'out':
        if 'glasses' in items:
            print('You can see the door at the end')
            final = input('Do you want to go to the door? (yes/no)').lower()
            if final == 'yes' or 'y':
                print('You scaped that horrible room and now you\'re free! Congratulations')
            else:
                print('You stayed too long in front of the light and now you have cancer. You lost :(')
        else:
            print('You\'re blind from that horrible light in the middle of the room. You lost.')
    else:
        print('You made a wrong answer you lost.')


if __name__ == '__main__':
    run()