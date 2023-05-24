def user_input():
    ask = int(input("Выбери ниже\n 1- записать пользователя\n"))
    return ask

def man():
    name = input("введите имя: ")
    family = input("введите фамилию: ")
    father = input("введите отчество: ")
    date = input("введите дату рождения: ")
    telephone = input("введите номер телефона:")
    data = name + "; " + family + "; "+ father +"; "+ date +"; " + telephone + "; " + "\n"
    return data

# def search():
#     str_search = input("строка для поиска  ")
#     return str_search
    