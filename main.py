from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# captcha = driver.find_element(By.LINK_TEXT, "Tentar uma imagem diferente")
# captcha.click()

events_dates = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
events_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget .menu a")

events = {}

for n in range(len(events_dates)):
    events[n] = {
        "time": events_dates[n].text,
        "name": events_names[n].text,
    }

print(events)

# bug_link_ie = driver.find_element(By.XPATH, value="colar-aqui-o-XPATH")


driver.quit()