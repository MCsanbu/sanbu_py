#  -*- coding: UTF-8 -*-

# MindPlus
# Python
import pyautogui
import time


time.sleep(1)
position_x ,position_y = pyautogui.position()
pyautogui.click(x=1849, y=369, clicks=2, interval=0.1, button='left')
time.sleep(1)
pyautogui.click(x=741, y=900, clicks=1, interval=0.1, button='left')