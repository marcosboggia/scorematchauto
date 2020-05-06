import os
import cv2

res_set = 'fullhd_240_full'

# Bluestacks
bluestacks_home = cv2.imread(f"images/{res_set}/bluestacks_home.PNG")
bluestacks_icon = cv2.imread(f"images/{res_set}/bluestacks_icon.PNG")
bluestacks_tab = cv2.imread(f"images/{res_set}/bluestacks_tab.PNG")
bluestacks_tab_x_folder = f"images/{res_set}/bluestacks_tab_x/"
bluestacks_tab_xs = [cv2.imread(bluestacks_tab_x_folder + img_path) for img_path in os.listdir(bluestacks_tab_x_folder)]
# Score Match
sm_arenas_btn = cv2.imread(f"images/{res_set}/sm_arenas_btn.PNG")
sm_openedcollect_background = cv2.imread(f"images/{res_set}/sm_openedcollect_background.PNG")
sm_aftercollecttick_btn = cv2.imread(f"images/{res_set}/sm_aftercollecttick_btn.PNG")
sm_socialsummary = cv2.imread(f"images/{res_set}/sm_socialsummary.PNG")
sm_exitsafemode_btn = cv2.imread(f"images/{res_set}/sm_exitsafemode_btn.PNG")
sm_back_btn = cv2.imread(f"images/{res_set}/sm_back_btn.PNG")
sm_closesummary_btn = cv2.imread(f"images/{res_set}/sm_closesummary_btn.PNG")
# Free collect buttons
freecollect_folder = f"images/{res_set}/freecollect/"
freecollect_icons = [cv2.imread(freecollect_folder + img_path) for img_path in os.listdir(freecollect_folder)]
# Ads X buttons
x_folder = 'images/x/'
ads_x = [cv2.imread(x_folder + img_path) for img_path in os.listdir(x_folder)]
ad_resumevideo_btn = cv2.imread(f"images/{res_set}/ads_resumevideo_btn.PNG")
