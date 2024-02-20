from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")


form1 = driver.find_element(By.NAME, value="fName")
form2 = driver.find_element(By.NAME, value="lName")
form3 = driver.find_element(By.NAME, value="email")
button = driver.find_element(By.CLASS_NAME, value="btn")

form1.send_keys("Lucas")
form2.send_keys("Fedrigo")
form3.send_keys("lucas.fedrigo@gmail.com")
button.send_keys(Keys.ENTER)


