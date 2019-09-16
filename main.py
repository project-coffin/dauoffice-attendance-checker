from selenium import webdriver
import sys

from settings import *

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
    driver.implicitly_wait(WAIT_SECONDS)

    input_ID = driver.find_element_by_name('username')
    input_ID.send_keys(LOGIN_INFO['ID'])

    input_PW = driver.find_element_by_name('password')
    input_PW.send_keys(LOGIN_INFO['PASSWORD'])

    button_login = driver.find_element_by_xpath('//*[@id="login_submit"]')
    button_login.click()

    driver.implicitly_wait(WAIT_SECONDS)


###########################
#  check
###########################

def is_checked(button):
    classes = button.get_attribute("class").split()

    return True if 'on' in classes else False


def check(check_option):
    driver.get(ATTEND_URL)
    driver.implicitly_wait(WAIT_SECONDS)

    if check_option == 'in':
        print(f'Hello, {Name}')
        button = driver.find_element_by_xpath('//*[@id="workIn"]')
    else:
        print(f'Bye, {Name}')
        button = driver.find_element_by_xpath('//*[@id="workOut"]')

    if not is_checked():
        button.click()
    else:
        print("You already checked.")


###########################
#  main
###########################

if __name__ == "__main__":
    check_option = sys.argv[1]

    if check_option not in ["in", "out"]:
        print("Please write : 'python main.py in' or 'python main.py out'")
        return

    driver = webdriver.Chrome(CHROMEDRIVER_PATH)

    while not is_login():
        WAIT_SECONDS += 1
        login(WAIT_SECONDS=WAIT_SECONDS)

    check(check_option)
    driver.close()
