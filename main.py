import pyautogui as pg
import time

pg.hotkey("win","r")
pg.typewrite("notepad\n")
time.sleep(1)
pg.typewrite("Hi im python")