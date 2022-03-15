import pyautogui as pg
import time

#Open execute
pg.hotkey("win","r")
#Go to notepad
pg.typewrite("notepad\n")
time.sleep(1)
time.sleep(1)
#Start conversation
pg.typewrite("Hi i'm python, your personal chatbot\n")
pg.sleep(2)
pg.typewrite("Sorry,...\n")
pg.sleep(1)
pg.typewrite("¿What's your name?\n")
pg.sleep(3)
pg.typewrite("Bye")