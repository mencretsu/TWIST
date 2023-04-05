import os, sys
import json
import pyfiglet
from time import sleep
from termcolor import colored

f = pyfiglet.Figlet(font="graffiti")
banner = colored(f.renderText("TWIST"), "green")
print(banner,colored("Twitter Shilling Bot | Github : @mencretsu\n","grey"))
usertweet = ""
while True: 
    if usertweet == "":
        print(colored("U're not login yet.","red"))
    else:print(f"Login as {usertweet}")
    print("\nMENU:\n1. Login\n2. Run\n3. Help\n4. Update")
    tinput = input("Input: ")

    if tinput == "1":
        while True:
            try:
                import login
                if login.SUCCESS == True:
                    usertweet = "jembot"
                    break
                else:
                    print("Error!")
                    pass
            except:pass
    if tinput == "2":
        pass
sleep(1000)
if tuser == "l" or tuser == "L":
    while True:
        prefix = False
        fake_name = input("enter project name: ")
        fake_text = input("enter text (max 280):")
        fake_prefix = input("use prefix? Y/N :")
        prefix_value = 0
        if fake_prefix == "y" or fake_prefix == "Y":
            prefix = True
            while True:
                try:
                    prefix_value = int(input('input prefix:'))
                    break
                except ValueError:
                    print("Invalid input, please enter a valid number :")
        else:pass
        print(fake_name,fake_text, prefix, prefix_value)
        data = {
            "fake_name": fake_name,
            "fake_text": fake_text,
            "use_prefix": prefix,
            "prefix_value": prefix_value
        }
        if os.path.exists("fake_data.json"):
            with open("fake_data.json", "r") as fle:
                all_data = json.load(file)
            all_data["fake"] = data
        else:
            all_data = [data]
        with open("fake_data.json", "w") as file:
            json.dump(all_data, file)
        fake =  input("data saved! \nback to menu/run? B/R :")
        if fake == "r" or fake == "R":
            break
        else:pass
else:pass
fake_run = input("run bot? y/n:\n")
if fake_run == "y" or fake_run == "Y":
    import faketweet_twint
else:pass
