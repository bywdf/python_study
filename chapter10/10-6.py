print('enter "q" to quit ')

while 1:
    first_number = input('please input 1st number:')
    if first_number == 'q':
        break
    second_number = input('please input 2rd number:')
    if first_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print('please input number!')
    else:
        print(answer)