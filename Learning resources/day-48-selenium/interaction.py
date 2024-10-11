from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

# article_num = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
# # article_num.click()
#
# news = driver.find_element(By.LINK_TEXT, value="Site news")
# # news.click()
#
# # Find the "Search" <input> by Name
# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python", Keys.ENTER)

# Challenge: Automatically fillup sign up page
first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email_address = driver.find_element(By.NAME, value="email")
enter_button = driver.find_element(By.CSS_SELECTOR, value=".form-signin button")

first_name.send_keys("Rohan")
last_name.send_keys("Rahim")
email_address.send_keys("rohanrahim04@gmail.com")
enter_button.send_keys(Keys.ENTER)




# driver.quit()
