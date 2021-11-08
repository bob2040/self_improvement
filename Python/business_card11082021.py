def create_card():
    card = {}
    card['Name'] = input('Please input your name:')
    card['Phone'] = input('Please input your phone number:')
    card['Address'] = input('Please input your address:')
    return card


def show_card(card):
    print()
    print('Here is my business card:')
    print('%22s' % '_____________________')
    print('|%21s|' % '                     ')
    for k in card:
        s = '%7s : %-11s' % (k.center(7), card[k])
        print('|' + s + '|')
    print('|%21s|' % '_____________________')


show_card(create_card())
