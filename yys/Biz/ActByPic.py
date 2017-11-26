from Biz import BaseControl as gc


# define window judge fundtion
def is_at_explorer_window():
    return gc.has_pic("section17")
def is_at_section_door():
    return  gc.has_pic("exploreratdoor")
def is_at_fb_window():
    return  gc.has_pic("clockteam")
def is_at_has_enemy_window():
    return gc.has_pic("enemy")
def is_at_has_boss_window():
    return gc.has_pic("boss")
def is_at_has_box_window():
    return gc.has_pic("box")
def is_at_end_fight_window():
    return  gc.has_pic("endfight")
def is_at_open_box_window():
    return gc.has_pic("openbox")


#define click function
def click_goto_fb():
    return  gc.click_pic("exploreratdoor")
def click_section17():
    return gc.click_pic("section17")
def click_box():
    return gc.click_pic("box")
def click_boss():
    return gc.click_pic("boss")
def click_enemy():
    return gc.click_pic("enemy")
def click_pve_cost():
    return gc.click_pic("pvecost")
def click_end_fight():
    return  gc.click_pic("endfight")

# open box can not click ,must click other place
def click_open_box():
    return  gc.click_pic("pvecost")






