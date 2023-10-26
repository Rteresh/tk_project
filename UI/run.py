import tkinter

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import time


def create_order(settings, check_var_size, check_var_sauce, check_var_cola
                 , check_var_paymethod):
    driver = webdriver.Safari()
    driver.maximize_window()
    actions = ActionChains(driver)

    text = []

    try:
        with open('templates/text_entries.txt', 'r') as file:
            text = file.readlines()
    except FileNotFoundError:
        pass

    driver.get(settings.url1)
    if check_var_size == '2':
        driver.find_element(By.XPATH, '//*[@id="mainDiv"]/div[1]/ul[2]/li[19]/div[5]/div').click()
        time.sleep(settings.time_sleep)
    elif check_var_size == '1':
        driver.find_element(By.XPATH, '//*[@id="mainDiv"]/div[1]/ul[2]/li[19]/div[4]/div').click()
        time.sleep(settings.time_sleep)

    ips = driver.find_element(By.CLASS_NAME, 'select2-choice')
    ips.click()
    time.sleep(settings.time_sleep)
    ips.send_keys(text[0])
    time.sleep(settings.time_sleep)
    ips.send_keys(Keys.ENTER)
    time.sleep(settings.time_sleep)
    ips2 = driver.find_element(By.XPATH, '//*[@id="s2id_home-number-modal"]')
    ips2.click()
    time.sleep(settings.time_sleep)
    ips2.send_keys(text[1])
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
    username.send_keys(text[2])
    time.sleep(settings.time_sleep)

    mobile = driver.find_element(By.XPATH, '//*[@id="address_form"]/form/div[2]/input[2]')
    mobile.send_keys(text[3])
    time.sleep(settings.time_sleep)

    flat = driver.find_element(By.XPATH, '//*[@id="address_form"]/form/div[3]/div[3]/input')
    flat.send_keys(text[4])
    time.sleep(settings.time_sleep)

    entrance = driver.find_element(By.XPATH, '//*[@id="address_form"]/form/div[3]/div[4]/input')
    entrance.send_keys(text[5])
    time.sleep(settings.time_sleep)

    floor = driver.find_element(By.XPATH, '//*[@id="address_form"]/form/div[3]/div[5]/input')
    floor.send_keys(text[6])
    time.sleep(settings.time_sleep)

    intercom = driver.find_element(By.XPATH, '//*[@id="address_form"]/form/div[3]/div[6]/input')
    intercom.send_keys(text[7])
    time.sleep(settings.time_sleep)

    comment = driver.find_element(By.XPATH, '//*[@id="cartComment"]')
    comment.send_keys(text[8])
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

    time.sleep(15)
    driver.quit()


def save_text(text, filename):
    with open(filename, 'w') as file:
        file.write(text)


def show_text_entry_window(tk, root, geometry):
    entry_window = tk.Toplevel(root)
    entry_window.title('Настройки')
    entry_window.geometry(geometry)

    labels = ["Адрес доставки", "Номер Дома", "Имя", "Мобильный телефон", "квартира", "подъезд", "этаж", "домофон",
              "комментарий"]

    text_entries = []

    for i, label_text in enumerate(labels):
        label = tk.Label(entry_window, text=label_text, anchor='w', width=15)
        label.grid(row=i, column=0, padx=10, pady=5)
        entry = tk.Entry(entry_window)
        entry.grid(row=i, column=1, padx=10, pady=5)
        text_entries.append(entry)

    try:
        with open("templates/text_entries.txt", "r") as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                if i < len(text_entries):
                    text_entries[i].insert(0, line.strip())
    except FileNotFoundError:
        pass

    save_button = tk.Button(entry_window, text="Сохранить", command=lambda: save_entries(text_entries, entry_window))
    save_button.grid(row=9, column=0, columnspan=2, pady=10)


def save_entries(entries, window):
    text_to_save = "\n".join(entry.get() for entry in entries)
    save_text(text_to_save, "templates/text_entries.txt")
    window.destroy()


def check_is_empty(nums):
    is_empty = True
    try:
        with open("templates/text_entries.txt", "r") as file:
            lines = file.readlines()
            if (len(lines)) == nums:
                for line in lines:
                    if not line.strip():  # Если строка пуста (после удаления лишних пробелов)
                        is_empty = False  # Файл не пустой
                        break  # Мы уже нашли пустую строку, больше проверять не нужно
            else:
                is_empty = False
                return is_empty
    except FileNotFoundError:
        is_empty = False  # Если файл не найден, считаем его тоже не пустым
    return is_empty


def show_error(tk, root, geometry):
    entry_window = tk.Toplevel(root)
    entry_window.title('Ошибка')
    entry_window.geometry(geometry)

    label = tk.Label(entry_window, text='Проверь настройки', anchor='w', width=15)
    label.pack()

    button = tk.Button(entry_window, text="OK", command=entry_window.destroy)
    button.pack(pady=10)
