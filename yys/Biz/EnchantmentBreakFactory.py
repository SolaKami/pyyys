from Biz import ActByPic as act
from Biz import WindowInitial as wi
import  time




#  start enchantment break

def break_start():
    print("break start")

    for num in range(1,500):
        wi.set_window_top()
        goto_union_break()

    print("break end")
    return

def goto_union_break():
    if act.is_at_explorer_window():
        act.click_enchantment_break()
    elif act.is_at_readyforfight_window():
        act.click_readyforfight()
    elif act.is_at_lose_window():
        act.click_lose_window()
    elif act.is_at_end_fight_window():
        act.click_end_fight()
    elif act.is_at_enchantment_break_door_window():
        # at union dorr,then start to break
        if act.is_at_attack_break_window():
            print("case attack break")
            act.click_attack_break()
        elif act.is_at_self_break_door_window():
            act.click_union_break()
        elif act.is_at_union_break_door_window():
            # choose level less than 50
            print("start level choose")
            level = 0
            #if act.click_level40():
            #    print("40")
            #    level = 40
            if act.click_level30():
               print("30")
               level = 30
            elif act.click_level20():
                print("20")
                level = 20
            elif act.click_level10():
                print("10")
                level = 10
            else:
                print("slide")
                act.slide_up("medal",30)
            print("end level choose ")
            time.sleep(1)
    else:
        print("no fimilar window")
    return


break_start()