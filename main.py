import os
import sys
import pyfiglet
from termcolor import colored
from run import scraping, shilling

ok = False
username = ""

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def login_user():
    try:
        from login import login
        tusername, driver = login()
        if tusername:
            print(colored("Your twitter is online\n","green"))  
            ok = True
        else:
            print("Error!")
            return
        driver.quit()
        return
    except ImportError:
        print("Login module not found.")
        return
    except:
        print("An error occurred during login.")
        return
    main_menu()
def run_bot():
    sc = scraping()
    sh = shilling()
    print("Scrapping twitter...")
def show_help():
    clear()
    print("Help menu:")
    print("1. Login - log in to Twitter")
    print("2. Run - run the Twitter shilling bot")
    print("3. Help - show this help menu")
    print("4. Update - update the bot")
    print("\nTwitter account : https://t.me/EfaemService")
    input("\nPress 'ENTER' to continue")
def update_bot():
    print("Updating the bot...")
def main_menu():
    global ok, username
    options = {
        "1": login_user,
        "2": run_bot,
        "3": show_help,
        "4": update_bot,
    }
    while True:
        banner = colored(pyfiglet.Figlet(font="cricket").renderText("TWIST"), "yellow")
        print(banner, colored("Twitter Shilling Bot | Github : @mencretsu\n", "blue"))
        if not ok:
            try:
                from login import login
                tusername, driver = login()
                if tusername:
                    username = tusername
                    ok = True
            except ImportError:
                print("Login module not found.")
                tusername = ""
            except:
                print("An error occurred during login.....")
                tusername = ""
        if not username:
            tusername = ""
            print(colored("U're not logged in yet.\n", "red"))
        else:
            print(colored("Your twitter is online\n","green"))

        # driver.quit()
        print("1. Login")
        print("2. Run")
        print("3. Help")
        print("4. Update")
        print("5. Exit")
        choice = input("Input: ")
        if choice in options:
            options[choice]()
        else:
            print("Invalid input. Please try again.")
if __name__ == '__main__':
    main_menu()
