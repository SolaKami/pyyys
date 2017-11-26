from Biz import BaseControl as gc


# define window judge fundtion
def is_at_explorer_window():
    return gc.has_pic("enchantmentbreak")
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
def is_at_enchantment_break_door_window():
    return  gc.has_pic("enchantmentbreakdoor")
def is_at_self_break_door_window():
    return  gc.has_pic("selfmode")
def is_at_union_break_door_window():
    return  gc.has_pic("unionmode")
def is_at_attack_break_window():
    return  gc.has_pic("attackbreak")
def is_at_readyforfight_window():
    return  gc.has_pic("readyforfight")


def is_at_lose_window():
    return gc.has_pic("losewindow")

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

def click_enchantment_break():
    return gc.click_pic("enchantmentbreak")
def click_union_break():
    return gc.click_pic("unioninbreak")

def click_level40():
    return gc.click_pic_plus("level40",100,0)
def click_level30():
    return gc.click_pic_plus("level30",100,0)
def click_level20():
    return gc.click_pic_plus("level20",100,0)
def click_level10():
    return gc.click_pic_plus("level10",100,0)

def click_attack_break():
    return gc.click_pic("attackbreak")
def click_readyforfight():
    return gc.click_pic("readyforfight")
def click_lose_window():
    return gc.click_pic("losewindow")


def slide_up(picture_name,h):
    return gc.slide_up(picture_name,h)



