
# with open("learning_python.txt", encoding='UTF-8') as f:
#     contents = f.read()        #  .read()整个读取为一整个内容
#     print(contents)

filename = 'learning_python.txt'
# with open(filename, encoding='utf-8') as f:
#     for line in f:
#         print(line.rstrip())


with open(filename, encoding='utf-8') as f:
    lines = f.readlines()

for line in lines:
    print(line)