from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# WINDOW
GEOMETRY = "500x500+2100+150"
GEOMETRY_TOP_LEVEL = "500x500+2200+190"
TITTLE = "Заказ пиццы"

# Selenium
url1 = 'https://pzz.by/pizzas'
url_order = 'https://pzz.by/cart'
time_sleep = 3

address_street_delivery = 'Партизанский просп'
address_num_delivery = '34/1'

username = 'Роман'
mobile = '+375291424993'
flat = '89'
entrance = '1'
floor = '14'
intercom = '+'
comment = 'Пиццу без болгарского перца пожалуйста. Хорошего дня.'

LABELS = 9

