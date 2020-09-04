def make_great(names):
    i = 0
    while i < len(names):
        names[i] ="The great " + names[i]
        i += 1
    print(names)

f_names = ['1', '2', '3', '4', '5', '6']
make_great(f_names)