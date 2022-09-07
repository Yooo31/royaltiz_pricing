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
