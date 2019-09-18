import time
from selenium import webdriver
import sys

from settings import *
from profile import *


BASE_URL = f'https://{COMPANY_NAME}.daouoffice.com'
LOGIN_URL = BASE_URL + '/login'
ATTEND_URL = BASE_URL + '/app/ehr'


###########################
#  login
###########################


def is_login():
    return False if LOGIN_URL in driver.current_url else True


def login(WAIT_SECONDS=2):
    driver.get(LOGIN_URL)
    time.sleep(WAIT_SECONDS)

    driver.find_element_by_name('username').send_keys(LOGIN_INFO['ID'])
    driver.find_element_by_name('password').send_keys(LOGIN_INFO['PASSWORD'])

    button_login = driver.find_element_by_xpath('//*[@id="login_submit"]')
    button_login.click()

    time.sleep(WAIT_SECONDS)


###########################
#  check
###########################

def is_checked(button):
    classes = button.get_attribute("class").split()

    return True if 'off' in classes else False


def check_attendance(check_option):
    driver.get(ATTEND_URL)
    time.sleep(WAIT_SECONDS)

    if check_option == 'in':
        button = driver.find_element_by_xpath('//*[@id="workIn"]')
    else:
        button = driver.find_element_by_xpath('//*[@id="workOut"]')

    if is_checked(button):
        print("You already checked.")
    else:
        button.click()

###########################
#  main
###########################

if __name__ == "__main__":
    check_option = sys.argv[1]

    if check_option not in ["in", "out"]:
        print("Please write : 'python main.py in' or 'python main.py out'")
        sys.exit()

    driver = webdriver.Chrome(CHROMEDRIVER_PATH)

    login()

    while not is_login():
        WAIT_SECONDS += 1
        login(WAIT_SECONDS=WAIT_SECONDS)

    check_attendance(check_option)
    driver.close()
