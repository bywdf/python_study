file_name = 'guest.txt'
guest_name = input('please input your name!')

with open(file_name, 'w', encoding='utf-8') as f:     
    f.write(guest_name)
    f.write(guest_name)