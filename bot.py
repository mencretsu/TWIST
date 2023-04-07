# pip3 install git+https://github.com/JustAnotherArchivist/snscrape.git
import pandas as pd
import snscrape.modules.twitter as smt
import json
from time import sleep
from termcolor import colored
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException, NoSuchElementException, ElementNotInteractableException, WebDriverException

content = ""
def scraping():
    global content
    key = input("Please input any keyword ex: BTC or Elon Musk: ")
    max = int(input("Input number of tweet ex: 100: "))
    content = input("Input ur twitter text (max 280 char): ")
    scraper = smt.TwitterSearchScraper(key)
    tweets = []
    for i, tweet in enumerate(scraper.get_items()):
        data = [tweet.url]
        tweets.append(data)
        if i > max:
            break
    tweet_df = pd.DataFrame(tweets, columns=["# Twitter url"])
    tweet_df.to_csv("scrape.csv", index=False)
    print("scraping done")
def shilling():
    global content
    from login import login
    tusername, driver = login()
    total = 0
    with open('scrape.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        links = list(dict.fromkeys(line[0] for line in reader))
    for link in links:
        driver.get(link)
        sleep(60)
        try:
            driver.implicitly_wait(10)
            reply = driver.find_element(By.CSS_SELECTOR,'[data-testid="reply"]')
            driver.execute_script("arguments[0].scrollIntoView();", reply)
            reply.click()
            driver.implicitly_wait(10)
            driver.find_element(By.CSS_SELECTOR,'[data-testid="tweetTextarea_0"]').send_keys(str(content))
            driver.implicitly_wait(10)
            driver.find_element(By.CSS_SELECTOR,'[data-testid="tweetButton"]').click()
            try:
                driver.implicitly_wait(15)
                driver.find_element(By.XPATH, "//span[normalize-space()='View']").click()
                myurl = driver.current_url
                print("- "+str(myurl))
                total += 1
            except:
                warnings = driver.find_elements(By.XPATH, "//*[contains(text(), 'warning')]")
                errors = driver.find_elements(By.XPATH, "//*[contains(text(), 'error')]")
                if warnings or errors:
                    print(colored("There may be a problem with your account.","light_red"))
                    return
                driver.refresh()
                pass
        except(ElementClickInterceptedException, StaleElementReferenceException, WebDriverException, ElementNotInteractableException):
            pass
    print(colored(f"\nTotal sent: {total}","light_green"))
    input("\nPress 'ENTER' to continue")
    driver.quit()
if __name__ == '__main__':
    scraping()
    shilling()
