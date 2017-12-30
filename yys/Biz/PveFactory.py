from Biz import ActByPic as act
from Biz import WindowInitial as wi
import time
import pymouse

# define some pve mode here
# define gloable parameter
PVE_FB_COUNT = 1
PVE_MISS_COUNT = 0
PVE_FIGHT_COUNT = 0
TEAM_MODE = 0

# mode1:fb count
# mode2:win count
# mode3:loop
def start_section(section_num,control_mode,control_num,team_mode):
    print("pve mode start")
    global PVE_FB_COUNT
    global PVE_MISS_COUNT
    global TEAM_MODE

    if team_mode == 1:
        TEAM_MODE = 1

    if control_mode == 1:
        while PVE_FB_COUNT <= control_num:
            if PVE_MISS_COUNT > 50:
                PVE_MISS_COUNT = 0
                wi.set_window_top("阴阳师-网易游戏")
            goto_section(section_num)
    elif control_mode == 2:
        while PVE_FIGHT_COUNT < control_num:
            if PVE_MISS_COUNT > 50:
                PVE_MISS_COUNT = 0
                wi.set_window_top("阴阳师-网易游戏")
            goto_section(section_num)
    print("pve mode end")
    return



def goto_section(section_num):
    print("log:")
    global PVE_FB_COUNT
    global PVE_MISS_COUNT
    global PVE_FIGHT_COUNT
    global TEAM_MODE
    if act.is_at_fb_window():
        fb_loop()
    elif act.is_at_end_fight_window():
        print("the %d FB count and the %d win count" % (PVE_FB_COUNT, PVE_FIGHT_COUNT))
        act.click_end_fight()
    elif act.is_at_open_box_window():
        act.click_open_box()
        sleep2()
    elif act.is_at_explorer_window():
        if act.gc.has_pic("explorerbox"):
            act.gc.click_pic("explorerbox")
            sleep2()
        elif act.has_section(section_num):
            if PVE_FB_COUNT % 3 == 0:
                time.sleep(30)
            act.click_section(section_num)
            sleep2()
        else:
            print("section not found")
            act.slide_up("section",-300)
    elif act.is_at_win_window():
        act.click_win_window()
    elif act.is_at_readyforfight_window():
        change_dogcard()
    elif act.is_at_lose_window():
        act.click_lose_window()
    elif act.is_at_section_door():
        act.click_goto_fb(TEAM_MODE)
        PVE_FB_COUNT += 1
    else:
        PVE_MISS_COUNT += 1
    return


def fb_loop():
    if is_at_expfull_window():
        click_expfullclick()
        click_expfullcancel()
    elif is_at_novitality_window():
        raise
    elif act.is_at_has_box_window():
        act.click_box()
    elif act.is_at_has_boss_window():
        act.click_boss()
    elif act.is_at_has_enemy_window():
        act.click_enemy()
    else:
        act.click_pve_cost()
    return


def change_dogcard():
    global PVE_FIGHT_COUNT
    if act.gc.has_pic("cardn"):
        if act.gc.has_pic("cardssr"):
            act.gc.click_pic("cardn")
            print("click card n")
        else:
            print("n window ok")
            if act.gc.has_pic_plus("fightfull1",400,0,1200,800):
                moveto_full_card()
            else:
                act.click_readyforfight()
                PVE_FIGHT_COUNT += 1
                print("ready for fight")
    elif act.gc.has_pic("cardall"):
        click_card_all()
    # ready mode
    elif has_dogcard_full():
        click_flight_card_area()
    elif act.click_readyforfight():
        PVE_FIGHT_COUNT += 1
        print("ready for fight")


def is_at_novitality_window():
    return act.gc.has_pic("novitality")
def has_dogcard_full():
    return act.gc.has_pic_plus("levelfull",0,0,560,800)
def click_flight_card_area():
    return act.gc.click_pic_plus("readyforfight",-600,-100)
def click_card_all():
    return act.gc.click_pic("cardall")
def click_card_N():
    return act.gc.click_pic("cardn")
def moveto_full_card():
    print("start move to full card")
    res = act.gc.move_from_to("cardfull1","fightfull1")
    print("moveto res : %s "%res)
    return res
def click_for_card_change():
    return act.gc.click_pic("readyforfight")



def is_at_level_full_window():
    return act.gc.has_pic("levelfull")
def is_at_expfull_window():
    return act.gc.has_pic("expfull")
def click_expfullclick():
    res = act.gc.click_pic("expfullclick")
    sleep1()
    return res
def click_expfullcancel():
    return act.gc.click_pic("expfullcancel")


def sleep1():
    time.sleep(1)
    return
def sleep2():
    time.sleep(2)
    return


if __name__ == '__main__':
    change_dogcard()