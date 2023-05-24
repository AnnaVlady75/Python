def add_dat(data):
    with open("db.txt", "w") as file:
        file.write(data)
    # print("Тел книга обновлена \n")   