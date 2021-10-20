from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

import time
def input():
    put = input("Please enter something")


def page_load_condition(driver, locator, wait_time=3):
    #wait time should be the condition for a loop that waits then tries to find the element
    count = 0
    while (count <= wait_time):
        time.sleep(1)
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, locator)))
            return
        except:
            print(f"Failed to load, try {count + 1} of {wait_time}")
            pass
    print("The page did not load")
    driver.quit()

def login(driver):
    #Find the three relevant page sections
    username_field = driver.find_element_by_css_selector("#userNameInput")
    password_field = driver.find_element_by_id("passwordInput")
    submit_btn = driver.find_element_by_id("submitButton")

    #Get the login details
    file = open('../login.txt', 'r')
    username = file.readline()
    password = file.readline()
    file.close()

    #Enter the login details
    username_field.send_keys(username)
    password_field.send_keys(password)
    submit_btn.click()

def pick_time_slot(driver, slot_num):
    #wait
    reserve_btns = driver.find_elements_by_css_selector(".booking-slot-item button")
    time.sleep(2)
    reserve_btn = reserve_btns[slot_num]
    reserve_btn.click()
    time.sleep(2)

def main():
    # Loads the first page
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("https://rec.carleton.ca/Account/Login")
    assert "Portal" in driver.title

    #Sets the implicit wait time to 10 seconds
    driver.implicitly_wait(10)

    element = driver.find_element_by_css_selector("[title~='Description']")
    #page_load_condition("loginModalContainer")
    
    element.click()
    #page_load_condition("userNameInput")

    login(driver)

    #page_load_condition("LogoBackground")
    driver.get("https://rec.carleton.ca/booking")
    #page_load_condition("NewBooking")
    
    #Navigates to the new booking page
    btn_list = driver.find_elements_by_css_selector("a.inherit-link")
    fitness_btn = btn_list[0]
    link_extension = fitness_btn.get_attribute("href")
    driver.get(link_extension)

    #On new page this finds the selectable dates
    date_btn_list = driver.find_elements_by_css_selector(".flex-center .btn")
    #could make this choose any of them from the list based on their dates? for now just always picks the last item
    time.sleep(2)
    date_btn_list[len(date_btn_list) - 1].click()

    pick_time_slot(driver, 3)

    driver.close()


if __name__ == "__main__":
    main()


