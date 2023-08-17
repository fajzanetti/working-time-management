import os

def clear_screen():
    os.system('clear')

def mark_point():
    clear_screen()
    os.system('python3 time.py')

def search_point():
    clear_screen()
    os.system('python3 search.py')

def main():
    options = {
        '1': mark_point,
        '2': search_point
    }

    while True:
        clear_screen()
        print("┏━━━┓")
        print("┃ 1 ╉╼ Marcar ponto")
        print("┃ 2 ╉╼ Pesquisa ponto")
        print("┗━┯━┛")
        print("┏━┷━┓")
        print("┃ 0 ╉╼ Sair")
        print("┗━┯━┛")

        option = input("  ╰──╼ Opção: ")

        if option == '0':
            break
        elif option in options:
            options[option]()
        else:
            clear_screen()

if __name__ == "__main__":
    main()
