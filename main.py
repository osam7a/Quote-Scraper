# Importing
from custom_logging import *
info("Importing Packages...")
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
info("Packages imported.", True)

info("Setting up driver options...")
options = Options()
options.headless = True
options.add_argument("--incognito")
options.add_argument("--log-level=3")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
info("Options set.", True)

info("Opening browser...")
driver = webdriver.Chrome(options=options)
driver.get("https://quotes-generator.com/quotes-generator.php")
info("Browser opened.", True)

info("Getting quote list...")
select = Select(driver.find_element(by=By.NAME, value="filter_category"))
categories = select.options[0:]
custom_input("Select a category\n" + catgoriesSTR)
button = driver.find_element(by=By.ID, value="new-quote")
button.click()
WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "quotes-content")))
info("Quote list obtained.", True)

info("Scraping quote list...")
soup = BeautifulSoup(driver.page_source, features="lxml")
quotes = []
for content in soup.find_all("div", {"class": "quotes-content"}):
    for _i, page in enumerate(content.children):
        try:
            for col in page.children:
                for _j, quote in enumerate(col.children):
                    quote = list(quote.children)[0]
                    author = list(quote.children)[3].text
                    qt = list(quote.children)[1].text
                    quotes.append(f"\"{qt}\" {author}")
        except: continue
info("Quote list scraped.", True)
quotes = [i for i in quotes]
f = open("quotes.txt", "w")
f.close()
f = open("quotes.txt", "a+")
if input("Would you like to save into file or get random quote? (1/2) ") == "1":
    for _i, quote in enumerate(quotes):
        try:
            f.write(quote + "\n" if _i != len(quotes) - 1 else quote)
        except UnicodeEncodeError:
            warning(f"Skipping unicode encode error ({_i}/{len(quotes)})")
            continue
    f.close()
else:
    print(random.choice(quotes))
    f.close()