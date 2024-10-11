from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep chrome browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# price_whole = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
# price_decimal = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
# print(f"The pot price is: {price_whole}.{price_decimal}")

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
#
# jobs_link = driver.find_element(By.CSS_SELECTOR, value=".jobs-widget a")
# print(jobs_link.text)

# # XPath
# help_and_contact_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[1]/a')
# print(help_and_contact_link.text)

# Challenge: Print the event dates from python.org
event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
# using dictionary comprehension
events = { n: {"time": event_times[n].text, "name": event_names[n].text} for n in range(len(event_times))}
print(events)



# driver.close() # for closing a webpage
driver.quit() # for closing the whole browser
