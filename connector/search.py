"""
    require: python 3.6, selenium module, webdriver
    @author: Vasily Jin
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options  

from getpass import getpass
import sys
import re
import time


def exist_user():
    try:
        error_span = wait.until(EC.visibility_of_element_located((By.ID, "session_key-login-error")))
        no_exist_user_alert = error_span.text
        print (no_exist_user_alert)
        return False
    except Exception as e:
        return True


def suspended_user():
    pass

def limited_user():
    pass

def pinverify():
    try:
        pin_input_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#verification-code")))
        pin_submit_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#btn-primary")))
        print("Please check your email address to verify.....")
        pincode = raw_input("Enter pin code:")
        pin_input_box.clear()
        pin_input_box.send_keys(pincode)
        pin_submit_btn.click()
        return True
    except Exception as e:
        return False
    


if __name__ == '__main__':
    
    user_email = raw_input("Enter email address:")
    user_password = getpass("Enter password:")

    options = Options()
    options.add_argument('--headless')
    
    driver = webdriver.Firefox(options=options)
    driver.get("https://www.linkedin.com")
    wait = WebDriverWait(driver, 5)

    print("----working-----")

    email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#login-email")))
    print("------pass email---------")

    password = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#login-password")))
    print("------pass password---------")

    signin_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#login-submit")))
    print("------pass button---------")

    email.clear()
    password.clear()

    email.send_keys(user_email)
    password.send_keys(user_password)

    signin_button.click()
    print("----------click sign in----------------")

    # check if user is exist
    if exist_user():
        print("That user is an existing user.")
    else:
        print("That user is not exist in Linkedin.")

    # pin code verification
    if pinverify():
        print("Success to verify!")
    else:
        print("sucessfull login without pin code verification!")
    
    # search connection
    search_input = driver.find_element_by_xpath("/html/body/nav/div/form/div/div/div/artdeco-typeahead-deprecated/artdeco-typeahead-deprecated-input/input")
    keyword = input("Input keyword:")
    search_input.clear()
    search_input.send_keys(keyword)
    search_input.send_keys(Keys.ENTER)
    print("-------click search button-----------")

    for i in range(2):
        time.sleep(5)
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(5)
        actor_name_lists = driver.find_elements_by_class_name("actor-name")
        actor_title_company_lists = driver.find_elements_by_class_name("subline-level-1")
        actor_location_lists = driver.find_elements_by_class_name("subline-level-2")

        for actor_name_list in actor_name_lists:
            actor_name = actor_name_list.text
            print (actor_name.encode('utf-8'))

        for actor_title_company_list in actor_title_company_lists:
            actor_title_company = actor_title_company_list.text
            if " at " in actor_title_company:
                title_company = actor_title_company.split(" at ")
                actor_title = title_company[0]
                actor_company = title_company[1]
                print (actor_company)
                print (actor_title)
        
        for actor_location_list in actor_location_lists:
            actor_location = actor_location_list.text
            print (actor_location)

        # store DB

        driver.find_element_by_class_name("next").click()
