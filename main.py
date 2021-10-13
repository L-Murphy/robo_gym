from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

import time

def page_load_condition(locator, wait_time=10):
    try:
        time.sleep(2)
        condition = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.ID, locator))
        )
    finally:
        print("Page did not load")
        driver.quit()


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://rec.carleton.ca/Account/Login")
assert "Portal" in driver.title
element = driver.find_element_by_css_selector("[title~='Description']")
#page_load_condition("loginModalContainer")
driver.implicitly_wait(100)
element.click()
#works to here
driver.implicitly_wait(1000)
#page_load_condition("userNameInput")

username_field = driver.find_element_by_css_selector("#userNameInput")
password_field = driver.find_element_by_id("passwordInput")
submit_btn = driver.find_element_by_id("submitButton")
driver.implicitly_wait(10)

file = open('../login.txt', 'r')
username = file.readline()
password = file.readline()
file.close()

username_field.send_keys(username)
password_field.send_keys(password)
submit_btn.click()

#page_load_condition("LogoBackground")
driver.get("https://rec.carleton.ca/booking")
#page_load_condition("NewBooking")
btn_list = driver.find_elements_by_css_selector("a.inherit-link")
fitness_btn = btn_list[0]
link_extension = fitness_btn.get_attribute("href")

driver.get(link_extension)
date_btn_list = driver.find_elements_by_css_selector(".flex-center .btn")
#could make this choose any of them from the list based on their dates? for now just always picks the last item
time.sleep(10)
date_btn_list[len(date_btn_list) - 1].click()

#wait
#driver.find_element_by_css_selector("6 - 7:30 AM")
time.sleep(10)

driver.close()


