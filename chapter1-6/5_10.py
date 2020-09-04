names = ["zhangsan", "lisi", "Wanger"]

for name in names:
    if name.lower() == "wanger":
        print("sorry, we have it")
    else:
        print("welcome " + name.title())


names.clear()
print(names)