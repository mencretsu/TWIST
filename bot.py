import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import json
from time import sleep
chromedriver_autoinstaller.install()
import getpass

def login():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # chrome_options.headless = True
    driver = webdriver.Chrome(options=chrome_options)
    try:
        with open('cookies.json', 'r') as f:
            cookies = json.load(f)
        driver.get('https://twitter.com')
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.refresh()
        wait = WebDriverWait(driver, 20)
        username_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="AppTabBar_Profile_Link"]')))
        username = username_element.get_attribute("href").split("/")[-1]
        driver.implicitly_wait(10)
        warnings = driver.find_elements(By.XPATH, "//*[contains(text(), 'warning')]")
        errors = driver.find_elements(By.XPATH, "//*[contains(text(), 'error')]")
        if warnings or errors:
            print("There may be a problem with your account.")
            username = ""
            driver.quit()
        
        tusername = str(username)
        return tusername, driver
    except:
        while True:
            print("Login to Twitter")
            tusername = input("Username/mail/phone : ")
            tpass = getpass.getpass(prompt="Password : ")
            driver.get("https://twitter.com/login")
            driver.implicitly_wait(15)

            userinput = driver.find_element(By.NAME, "text")
            userinput.send_keys(tusername)
            userinput.send_keys(Keys.ENTER)
            try:
                element_present = EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="toast"]'))
                WebDriverWait(driver, 10).until(element_present)
                print("Error can't find ur account")
                continue
            except:
                print("email verified")

            driver.implicitly_wait(15)
            passinput= driver.find_element(By.NAME, "password")
            passinput.send_keys(tpass)
            passinput.send_keys(Keys.ENTER)
            try:
                element_present = EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="toast"]'))
                WebDriverWait(driver, 10).until(element_present)
                print("Error: Invalid password")
                continue
            except:
                print("Login successful")
                cookies = driver.get_cookies()
                if warnings or errors:
                    print("There may be a problem with your account.")
                    username = ""
                    driver.quit()
                    break
                with open('cookies.json', 'w') as f:
                    json.dump(cookies, f)
                return tusername, driver
            
