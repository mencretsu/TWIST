import pandas as pd
import snscrape.modules.twitter as smt
import json
import csv
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
def shilling():
    global content
    from login import login
    tusername, driver = login()
    driver.set_window_size(800, 600)
    total = 0
    with open('scrape.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        links = list(dict.fromkeys(line[0] for line in reader))
    print("\nRunning...\n")
    for link in links:
        driver.get(link)
        sleep(10)
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
                print(colored(f"- {myurl}", "blue"))
                total += 1
            except:
                try:
                    driver.implicitly_wait(5)
                    suspension = driver.find_element(By.XPATH, "//a[contains(@href, 'https://help.twitter.com/forms/general?utm_source=htl&utm_medium=suspension_banner&utm_campaign=suspension_banner_utm')]")
                    if suspension:
                        print("Your account is suspended.")
                        return
                except:
                    driver.refresh()
                    pass
        except(ElementClickInterceptedException, StaleElementReferenceException, WebDriverException, ElementNotInteractableException):
            pass
    print(colored(f"\nTotal sent: {total}","light_green"))
    input("\nPress 'ENTER' to continue")
    driver.quit()
