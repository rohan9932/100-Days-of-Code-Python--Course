from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4033697762&f_AL=true&f_E=2&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER")

# sign in
sign_in_btn = driver.find_element(By.CSS_SELECTOR, value=".nav__cta-container .nav__button-secondary")
sign_in_btn.click()

email = driver.find_element(By.NAME, value="email-or-phone")
password = driver.find_element(By.NAME, value="password")
submit_btn = driver.find_element(By.ID, value="join-form-submit")
email.send_keys("test.rohan932@gmail.com")
password.send_keys("rumizaman1978")
submit_btn.click()


