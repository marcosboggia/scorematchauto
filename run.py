from image_loader import *
from watchdog import timed, report_success

from gui_automation import GuiAuto
from time import sleep
from db.db import create_ads_count, add_count


run_id = None


# GuiAuto
ga = GuiAuto()


@timed()
@report_success()
def open_game():
    print("Opening game", end='')
    while not ga.detect(bluestacks_icon, 0.99):
        sleep(0.5)
    sleep(1)
    ga.click()

    return True


@timed()
@report_success()
def main_menu():
    print("Main menu", end='')
    # WAIT FOR APP TO OPEN AND SEE IF
    #   SUMMARY APPEARED
    #   SAFEMODE APPEARED
    #   OPENED NORMALLY AND ARENA BUTTON BECOMES AVAILABLE
    while True:
        if ga.detect(sm_socialsummary, 0.99):
            pass  # Click X
            break
        if ga.detect(sm_exitsafemode_btn, 0.99):
            pass  # Exit safe mode
            break
        if ga.detect(sm_arenas_btn, 0.99):
            ga.click()
            sleep(1)
            break
        sleep(0.5)
    # GO BACK TO MAKE SURE FREE COLLECT BTN APPEARS
    while not ga.detect(sm_back_btn, 0.99):
        ga.click()

    return True


@timed()
@report_success()
def freecollect():
    print("Freecollect", end='')
    while True:
        for each in freecollect_icons:
            if ga.detect(each, 0.99):
                ga.click()
                return True


@timed()
@report_success()
def ad():
    print("Ad", end='')
    while True:
        # LOOK FOR X
        for each in ads_x:
            if ga.detect(each, 0.98):
                ga.click()
                print('found x', end='', flush=True)
                sleep(0.5)
                # RESUME VIDEO
                if ga.detect(ad_resumevideo_btn, 0.99):
                    ga.click()
                    sleep(30)
                else:
                    return True


@timed()
@report_success()
def collect_rewards():
    print("Collect", end='')
    # WAIT FOR BACKGROUND
    while not ga.detect(sm_openedcollect_background, 0.99):
        pass
    coords = ga.spot.center()
    # WAIT FOR BLUE TICK
    while not ga.detect(sm_aftercollecttick_btn, 0.99):
        ga.click(coords=coords)  # Click background until tick appears
    sleep(1)
    ga.click()  # Click tick
    add_count(run_id)  # Count ads opened

    return True


@timed()
@report_success()
def close_game():
    print("Closing game", end='')
    while not ga.detect(bluestacks_tab, 0.9):
        sleep(0.5)
    ga.move()
    sleep(0.5)
    while not ga.detect(bluestacks_tab_x, 0.99):
        sleep(0.5)
    sleep(0.5)
    ga.click()

    return True


if __name__ == "__main__":
    run_id = create_ads_count()
    while True:
        if not open_game():
            close_game()
            continue
        if not main_menu():
            close_game()
            continue
        if not freecollect():
            close_game()
            continue
        if not ad():
            close_game()
            continue
        if not collect_rewards():
            close_game()
            continue
        close_game()
