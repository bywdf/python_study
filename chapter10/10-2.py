with open('learning_python.txt',encoding = 'utf-8') as f_file:
    lines = f_file.readlines()

line_1 = ""
for line in lines:
    line_1 = line.replace('python', 'C++')
    print(line_1.strip())