from colorama import Fore
import data.mongo_setup as mongo_setup
import product_manager


def main():
    mongo_setup.global_init()
    print_header()
    try:
        while True:
            product_manager.run()
    except KeyboardInterrupt:
        return


def print_header():
    bakkal = \
        """
    ____        __   __         __
   / __ )____ _/ /__/ /______ _/ /
  / __  / __ `/ //_/ //_/ __ `/ / 
 / /_/ / /_/ / ,< / ,< / /_/ / /  
/_____/\__,_/_/|_/_/|_|\__,_/_/   """
    print(Fore.WHITE + '*********************************************')
    print(Fore.GREEN + bakkal)
    print(Fore.WHITE + '*********************************************')
    print()
    print("Welcome to Bakkal product terminal!")
    print()

if __name__ == '__main__':
    main()