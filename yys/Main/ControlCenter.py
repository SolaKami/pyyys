from Biz import WindowInitial
from Biz import PveFactory
import time

#name="阴阳师 - MuMu模拟器"
name="阴阳师-网易游戏"
# start process
# initial
#WindowInitial.set_window_top()
WindowInitial.ini_game_window(name)
time.sleep(2)

#choose auto mode
PveFactory.start_section(2,1,10,1)

# close window
# time.sleep(600)
# WindowInitial.close_window(name)
# print("window close")




