# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qLvTnyUxxEtb88Y3BUCFDKb1uZjT3mTi
"""

import pyautogui
import time

def screenshot():
  name =  int(round(time.time() * 1000))
  name =  '{}.png'.format(name)
  time.sleep(5)
  img =  pyautogui.screenshot(name)
  img.show()

screenshot()