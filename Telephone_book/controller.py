import view
import database

def main():
    while  True:
        ask = view.user_input()
        if ask == 1:
            data = view.man()
            database.add_dat(data)

main()            
