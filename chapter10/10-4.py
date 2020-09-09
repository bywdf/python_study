file_name = 'guest_book.txt'

while True:
    guest_name = input('please input your name:')
    if guest_name == 'quit':
        break
    else:
        with open(file_name, 'a', encoding='utf-8') as f:
            f.write(guest_name + '\n')
        print('Hello '+ guest_name + ' u have ...')