from Biz import ActByPic as act
from Biz import WindowInitial as wi

# define some pve mode here
# define gloable parameter
PVE_FB_COUNT = 0
PVE_MISS_COUNT = 0

# mode1:fb count
# mode2:time
# mode3:loop
def start_section(section_num,control_mode,control_num):
    print("pve mode start")
    global PVE_FB_COUNT
    global PVE_MISS_COUNT
    if control_mode == 1:
        while PVE_FB_COUNT < control_num:
            if PVE_MISS_COUNT > 50:
                PVE_MISS_COUNT = 0
                wi.set_window_top()
            print("FB_COUNT:", PVE_FB_COUNT)
            print("MISS_COUNT",PVE_MISS_COUNT)
            goto_section()
    print("pve mode end")
    return



def goto_section():
    global PVE_FB_COUNT
    global PVE_MISS_COUNT
    if act.is_at_explorer_window() == 1:
        act.click_section17()
    elif act.is_at_section_door() == 1:
        act.click_goto_fb()
        PVE_FB_COUNT += 1
    elif act.is_at_open_box_window() == 1:
        act.click_open_box()
    elif act.is_at_end_fight_window() ==1 :
        act.click_end_fight()
    elif act.is_at_fb_window() == 1:
        fb_loop()
    else:
        PVE_MISS_COUNT += 1
    return


def fb_loop():
    if act.is_at_has_box_window() == 1:
        act.click_box()
    elif act.is_at_has_boss_window() == 1:
        act.click_boss()
    elif act.is_at_has_enemy_window() == 1:
        act.click_enemy()
    else:
        act.click_pve_cost()
    return

