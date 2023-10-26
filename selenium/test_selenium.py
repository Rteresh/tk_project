from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import time
from UI import settings

check_var_size = '2'
check_var_sauce = False
check_var_paymethod = '2'
check_var_cola = False

driver = webdriver.Safari()
driver.maximize_window()
actions = ActionChains(driver)

driver.get(settings.url1)
if check_var_size == '1':
    driver.find_element(By.XPATH, '//*[@id="mainDiv"]/div[1]/ul[2]/li[19]/div[5]/div').click()
    time.sleep(settings.time_sleep)
elif check_var_size == '2':
    driver.find_element(By.XPATH, '//*[@id="mainDiv"]/div[1]/ul[2]/li[19]/div[4]/div').click()
    time.sleep(settings.time_sleep)
ips = driver.find_element(By.CLASS_NAME, 'select2-choice')
ips.click()
time.sleep(settings.time_sleep)
ips.send_keys(settings.address_street_delivery)
time.sleep(settings.time_sleep)
ips.send_keys(Keys.ENTER)
time.sleep(settings.time_sleep)
ips2 = driver.find_element(By.XPATH, '//*[@id="s2id_home-number-modal"]')
ips2.click()
time.sleep(settings.time_sleep)
ips2.send_keys(settings.address_num_delivery)
time.sleep(settings.time_sleep)
ips.send_keys(Keys.ENTER)
btn_access = driver.find_element(By.XPATH, '//*[@id="byaddress"]')
btn_access.click()
time.sleep(settings.time_sleep)
driver.get(settings.url_order)
if check_var_sauce:
    driver.find_element(By.XPATH, '//*[@id="cartContent"]/div[4]/ul/li[5]/div[3]/div/button').click()
    time.sleep(settings.time_sleep)
if check_var_cola:
    driver.find_element(By.XPATH, '//*[@id="cartContent"]/div[8]/ul/li[2]/div[3]/div/button').click()
    time.sleep(settings.time_sleep)
username = driver.find_element(By.XPATH, '//*[@id="address_form"]/form/div[1]/input')
username.send_keys(settings.username)
time.sleep(settings.time_sleep)

mobile = driver.find_element(By.XPATH, '//*[@id="address_form"]/form/div[2]/input[2]')
mobile.send_keys(settings.mobile)
time.sleep(settings.time_sleep)

flat = driver.find_element(By.XPATH, '//*[@id="address_form"]/form/div[3]/div[3]/input')
flat.send_keys(settings.flat)
time.sleep(settings.time_sleep)

entrance = driver.find_element(By.XPATH, '//*[@id="address_form"]/form/div[3]/div[4]/input')
entrance.send_keys(settings.entrance)
time.sleep(settings.time_sleep)

floor = driver.find_element(By.XPATH, '//*[@id="address_form"]/form/div[3]/div[5]/input')
floor.send_keys(settings.floor)
time.sleep(settings.time_sleep)

intercom = driver.find_element(By.XPATH, '//*[@id="address_form"]/form/div[3]/div[6]/input')
intercom.send_keys(settings.intercom)
time.sleep(settings.time_sleep)

comment = driver.find_element(By.XPATH, '//*[@id="cartComment"]')
comment.send_keys(settings.comment)
time.sleep(settings.time_sleep)

if check_var_paymethod == '1':
    radio1 = driver.find_element(By.XPATH, '//*[@id="address_form"]/form/div[12]/div[2]/label')
    radio1.click()
    time.sleep(settings.time_sleep)
elif check_var_paymethod == '2':
    radio1 = driver.find_element(By.XPATH, '//*[@id="address_form"]/form/div[12]/div[1]/label')
    radio1.click()
    time.sleep(settings.time_sleep)

radio2 = driver.find_element(By.XPATH, '//*[@id="runtimeDeliveryButton"]')
radio2.click()
time.sleep(settings.time_sleep)

# finish_btn = driver.find_element(By.XPATH, '//*[@id="address_form"]/div/div[2]/span')
# finish_btn.click()

driver.quit()
