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
  time.sleep(20)

def accept_cookies():
  print('start cookies')

  cookie_button = driver.find_element(By.CLASS_NAME, 'cookie-banner-accept-button') # Find the button to accept cookies
  cookie_button.click()

def start(player) :
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

def run_all_player() :
  for actual_player in player_list:
    print('Check for ' + actual_player)
    all_player_price.append(actual_player + ' = ')
    start(actual_player)