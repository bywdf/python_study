def make_great(yuanlai, guohou):
    while yuanlai:
        yuan = yuanlai.pop()
        guohou.append("the great " + yuan)
    print("yuanlaide",yuanlai)
    print("guhoude", guohou)

names = ['1', '2', '3', '4', '5', '6']
f_names = []

make_great(names, f_names)