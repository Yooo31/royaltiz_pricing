from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

player_list = ['DUPONT', 'HOUNKPATIN', 'TANGA', 'LANDU']
global all_player_price
all_player_price = []

def open_player_view(player=""):
  print('Opening the ' + player + ' player view')

  driver.get("https://www.royaltiz.com/" + player) # Go to the url of the website
  time.sleep(5)

def accept_cookies():
  print('start cookies')

  cookie_button = driver.find_element(By.CLASS_NAME, 'cookie-banner-accept-button') # Find the button to accept cookies
  cookie_button.click()

def get_player_price() :
  print('Start getting price')

  player_price = driver.find_element(By.XPATH, '//h3[@data-testid="talent-price"]').text # Find the card that contains the cashback
  driver.close() # Close the browser

  all_player_price.append(player_price + ' / ')

def start(player) :
  all_player_price.append(player + ' = ')

  chrome_options = Options()

  # Options to run without interface

  # chrome_options.add_argument("--no-sandbox")
  # chrome_options.add_argument("--headless")

  # Bypass the anti bot

  chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
  chrome_options.add_experimental_option('useAutomationExtension', False)
  chrome_options.add_argument("--disable-blink-features=AutomationControlled")

  # Create the driver

  global driver
  driver = webdriver.Chrome(executable_path="./chromedriver", options=chrome_options)

  # Launch the process

  open_player_view(player)
  accept_cookies()
  get_player_price()

def run_all_player() :
  for actual_player in player_list:
    print('Check for ' + actual_player)
    start(actual_player)

  answer_to_send = ''.join(str(x) for x in all_player_price)
  print(answer_to_send)

def get_one_player_price(name) :
  start(name)

  answer_to_send = ''.join(str(x) for x in all_player_price)
  print(answer_to_send)