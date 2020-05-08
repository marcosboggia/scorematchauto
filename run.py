from image_loader import *
from watchdog import timed, report_success

from gui_automation import GuiAuto
from time import sleep
from db import create_ads_count

# GuiAuto
ga = GuiAuto()

# Start to count opened ads and failed runs
run_id = create_ads_count()


@timed(run_id)
@report_success()
def open_game():
    print("Opening game", end='')
    while not ga.detect(bluestacks_home, 0.99):
        sleep(0.1)
    ga.click()
    while not ga.detect(bluestacks_icon, 0.99):
        sleep(0.5)
    sleep(1)
    ga.click()

    return True


@timed(run_id)
@report_success()
def main_menu():
    print("Main menu", end='')
    # WAIT FOR APP TO OPEN AND SEE IF
    #   SUMMARY APPEARED
    #   SAFEMODE APPEARED
    #   OPENED NORMALLY AND ARENA BUTTON BECOMES AVAILABLE
    sleep(10)  # Give time for Social summary to appear
    while True:
        # SOCIAL SUMMARY START
        if ga.detect(sm_socialsummary, 0.99):
            print(" social summary...", end='')
            sleep(1)
            while not ga.detect(sm_closesummary_btn, 0.99):
                pass
            print(" closing it...", end='')
            ga.click()
            break
        # SAFE MODE START
        if ga.detect(sm_exitsafemode_btn, 0.99):
            print(" safe mode...", end='')
            pass  # Exit safe mode
            break
        # NORMAL START
        if ga.detect(sm_arenas_btn, 0.99):
            print(" normal start...", end='')
            break
    while True:
        if ga.detect(sm_arenas_btn, 0.99):
            ga.click()
            sleep(1)
            break
    # GO BACK TO MAKE SURE FREE COLLECT BTN APPEARS
    while not ga.detect(sm_back_btn, 0.99):
        sleep(0.1)
        pass
    ga.click()

    return True


@timed(run_id, deadline=120)
@report_success()
def freecollect():
    print("Freecollect", end='')
    while True:
        for each in freecollect_icons:
            if ga.detect(each, 0.97):
                ga.click()
                return True


@timed(run_id)
@report_success()
def ad():
    modes = [
        {'handler': ga,
         'function': ga.detect,
         'threshold': 0.99}
    ]
    print("Ad", end='')
    while True:
        # LOOK FOR X
        for each in ads_x:
            for mode in modes:
                if mode['function'](each, mode['threshold']):
                    mode['handler'].click()
                    print(' found x', end='', flush=True)
                    sleep(5)
                    # RESUME VIDEO
                    if ga.detect(ad_resumevideo_btn, 0.98):
                        print(' found resume', end='', flush=True)
                        ga.click()
                        sleep(30)
                    else:
                        return True


@timed(run_id)
@report_success()
def collect_rewards():
    from db import add_count
    print("Collect", end='')
    # WAIT FOR BACKGROUND
    while not ga.detect(sm_openedcollect_background, 0.95):
        pass
    coords = ga.spot.center()  # Save coordinates for later
    # WAIT FOR BLUE TICK
    while not ga.detect(sm_aftercollecttick_btn, 0.99):
        ga.click(coords=coords)  # Click background until tick appears
    sleep(1)
    ga.click()  # Click tick
    add_count(run_id)  # Count ads opened

    return True


@timed(run_id)
@report_success()
def close_game():
    print("Closing game", end='')
    while not ga.detect(bluestacks_tab, 0.9):
        sleep(0.5)
    ga.move()
    sleep(0.5)
    while True:
        for each in bluestacks_tab_xs:
            if ga.detect(each, 0.99):
                sleep(0.5)
                ga.click()
                return True


if __name__ == "__main__":
    print("Starting...")
    while True:
        print()
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
