# using command prompt, do "pip install " followed by the library name for all imported libraries
# example for what to type in: pip install inflect
# do this for all, don't include the as pd and as pg parts for their respective libraries
import inflect
import pyautogui as pg
import pydirectinput as pd
import time
from pynput.keyboard import Key, Controller
keyboard = Controller()
numq = int(input("How many grammar jacks do you want to do?"))
num = (numq+1)  
print("You have 5 seconds to go to input area.")
time.sleep(5)

p = inflect.engine()
for x in range (1, num):
    c = p.number_to_words(x)
    pd.press('/')
    pg.typewrite(c.capitalize()+("."))
    pd.press('enter')
    pd.press('space')
    time.sleep(1.5)

