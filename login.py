import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import time
import json
from termcolor import colored

SUCCESS = False

while not SUCCESS:
    tusername = input("Twitter username/mail/phone : ")
    tpass = input("Password : ")
    print("checking.. please wait..")
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.headless = True
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://twitter.com/login")

        driver.implicitly_wait(15) #change this according to your load driver speed/u can also use webdriverwait
        userinput = driver.find_element(By.NAME, "text")
        userinput.send_keys(tusername)
        userinput.send_keys(Keys.ENTER)
        try:
            element_present = EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="toast"]'))
            WebDriverWait(driver, 10).until(element_present)
            print(colored("Error can't find ur account","red"))
            continue
        except:
            print(colored("email verified","green"))
        driver.implicitly_wait(15)
        passinput= driver.find_element(By.NAME, "password")
        passinput.send_keys(tpass)
        passinput.send_keys(Keys.ENTER)
        try:
            element_present = EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="toast"]'))
            WebDriverWait(driver, 10).until(element_present)
            print(colored("Error: Invalid password","red"))
            continue
        except:
            print(colored("Login successful","green"))
            SUCCESS = True
    except:
        print(colored("ERROR MSG: Login invalid","red"))
        SUCCESS = False
    driver.quit()
