from Biz import ActByPic as act
from Biz import WindowInitial as wi
from Biz import BaseControl as bc
import  time


BREAK_WIN_COUNT = 0
BREAK_MISS_COUNT = 0
BREAK_MODE = 0
BREAK_NEXT_COUNT = 0

#  start enchantment break
def break_start(mode,breakcount):
    print("start wait")
    global BREAK_WIN_COUNT
    global BREAK_MODE
    global BREAK_NEXT_COUNT
    BREAK_MODE = mode
    while(BREAK_WIN_COUNT<breakcount and BREAK_NEXT_COUNT < 3):
        goto_union_break()
    print("break end")
    return

def goto_union_break():
    global BREAK_MISS_COUNT
    global BREAK_WIN_COUNT
    if act.is_at_enchantment_break_door_window():
        # at union door,then start to break
        break_loop()
    elif act.is_at_readyforfight_window():
        act.click_readyforfight()
    elif act.is_at_end_fight_window():
        print("the %d win count" % BREAK_WIN_COUNT)
        act.click_end_fight()
    elif act.is_at_explorer_window():
        act.click_enchantment_break()
    elif act.is_at_lose_window():
        act.click_lose_window()
    elif act.is_at_win_window():
        act.click_win_window()
    else:
        BREAK_MISS_COUNT += 1
        if BREAK_MISS_COUNT >=50:
            BREAK_MISS_COUNT = 0
            wi.set_window_top("阴阳师-网易游戏")
    return


def break_loop():
    global BREAK_WIN_COUNT
    if act.is_at_attack_break_window():
        print("at attack break window")
        sleep1()
        res = act.click_attack_break()
        BREAK_WIN_COUNT += 1
        print("double click result: %s"%res)
        sleep1()
    elif act.is_at_self_break_door_window():
        act.click_union_break()
    elif act.is_at_union_break_door_window():
        # judge left count,if 0 ,goto next,else start break
        if is_left_0_break_count() == 0:
            goto_next_union()
            print("goto next union  BY 0 COUNT")
        else:
            level = 0
            if is_at_breaked_window():
                # not find fit level,if see break,then this union is end
                goto_next_union()
                print("goto next union BY NO SMALL PEOPLE")
            # elif BREAK_MODE >= 60 and act.click_level0():
            #     level = 60
            # elif BREAK_MODE >= 40 and act.click_level40():
            #    level = 40
            elif act.is_at_break_loss_window():
                print("find break loss")
                act.slide_up("breakloss", 400)
            elif BREAK_MODE >= 30 and act.click_level30():
                sleep1()
            elif BREAK_MODE >= 20 and  act.click_level20():
                sleep1()
            elif BREAK_MODE >= 10 and  act.click_level10():
                sleep1()
            else:
                act.slide_up("medal", 400)

def is_left_0_break_count():
    if bc.has_pic("num0") == 0:
        return 1
    else:
        return 0

def goto_next_union():
    global BREAK_NEXT_COUNT
    BREAK_NEXT_COUNT += 1
    if is_at_1_union_window():
        click_2_union()
    elif is_at_3_union_window():
        click_1_union()
    else:
        click_3_union()

def is_at_1_union_window():
    return bc.has_pic("union1")
def is_at_3_union_window():
    return bc.has_pic("union3")
def is_at_breaked_window():
    return bc.has_pic("breakwin")

def click_1_union():
    return bc.click_pic_plus("unionmode",-200,100)
def click_2_union():
    return bc.click_pic_plus("unionmode",-200,250)
def click_3_union():
    return bc.click_pic_plus("unionmode",-200,420)

def sleep1():
    time.sleep(1)
    return

