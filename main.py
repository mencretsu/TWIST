import os, sys
import pyfiglet
from termcolor import colored
import bot as botting
import subprocess
import importlib

with open('requirements.txt') as f:
    required_modules = f.read().splitlines()

for module in required_modules:
    try:
        importlib.import_module(module)
    except ImportError:
        subprocess.call(['pip', 'install', module])
ok = False
username = ""

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def login_user():
    try:
        from login import login
        tusername, driver = login()
        if tusername:
            print(colored(f"~ Login as @{tusername}\n", "light_green"))
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
        print(colored("An error occurred during login.","light_red"))
        return
    main_menu()
def run_bot():
    if not username:
        print(colored("\nTo run this bot, you need a Twitter account. Please login first!\n", "yellow"))
        input("\nPress 'ENTER' to go back")
        main_menu()
    botting()
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
    subprocess.run(["pip", "install", "--upgrade", "git+https://github.com/mencretsu/twist.git"])
    input("\nPress 'ENTER' to continue")
def main_menu():
    global ok, username
    
    options = {
        "1": login_user,
        "2": run_bot,
        "3": show_help,
        "4": update_bot,
    }
    while True:
        clear()
        banner = colored(pyfiglet.Figlet(font="graffiti").renderText("TWIST"), "cyan")
        print(banner, colored("Twitter Shilling Bot | Github : @mencretsu\n","white","on_cyan"))
        # if not ok:
        #     try:
        #         from login import login
        #         tusername, driver = login()
        #         if tusername:
        #             username = tusername
        #             ok = True
        #     except ImportError:
        #         print("Login module not found.")
        #         tusername = ""
        #     except:
        #         print("An error occurred during login.....")
        #         tusername = ""
        if not username:
            tusername = ""
            print(colored("~ U're not logged in yet.\n", "light_red"))
        else:
            print(colored(f"~ Login as @{tusername}\n", "light_green"))
        # driver.quit()
        print("1. Login")
        print("2. Run")
        print("3. Help")
        print("4. Update")
        choice = input(colored("Input: ","cyan"))
        if choice in options:
            options[choice]()
        else:
            print("Invalid input. Please try again.")
if __name__ == '__main__':
    main_menu()
