favorite_languages = {
    "zhangsan":"C",
    "lisi":"python",
    "wangwu":"java",
    "lucy":"R",
    "lili":"go",
}

#for name, language in favorite_languages.items():
   # print(f"{name} language is {language}")

search_names = ["zhangsan", "lisi", "wangwu", "hailu", "sunsan"]
for search_name in search_names:
    if search_name in favorite_languages.keys():
        print(f"{search_name} u have searched")
    else:
        print(f"{search_name} pls search")