import pyautogui as pg
import time

pg.hotkey("win","r")
pg.typewrite("notepad\n")
time.sleep(1)
pg.typewrite("Hi i'm python\n")
pg.sleep(2)
pg.typewrite("Sorry,...\n")
pg.sleep(1)
pg.typewrite("¿What's your name?\n")
