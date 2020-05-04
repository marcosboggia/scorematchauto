import os
import cv2

res_set = 'fullhd_240_default'

# Bluestacks
bluestacks_icon = cv2.imread(f"images/{res_set}/bluestacks_icon.PNG")
bluestacks_tab = cv2.imread(f"images/{res_set}/bluestacks_tab.PNG")
bluestacks_tab_x = cv2.imread(f"images/{res_set}/bluestacks_tab_x.PNG")
# Score Match
sm_arenas_btn = cv2.imread(f"images/{res_set}/sm_arenas_btn.PNG")
sm_openedcollect_background = cv2.imread(f"images/{res_set}/sm_openedcollect_background.PNG")
sm_aftercollecttick_btn = cv2.imread(f"images/{res_set}/sm_aftercollecttick_btn.PNG")
sm_socialsummary = cv2.imread(f"images/{res_set}/sm_socialsummary.PNG")
sm_exitsafemode_btn = cv2.imread(f"images/{res_set}/sm_exitsafemode_btn.PNG")
sm_back_btn = cv2.imread(f"images/{res_set}/sm_back_btn.PNG")
# Free collect buttons
freecollect_icons = [
    cv2.imread(f"images/{res_set}/freecollect/sm_freecollect_btn_red.PNG"),
    cv2.imread(f"images/{res_set}/freecollect/sm_freecollect_btn_silver.PNG")
]
# Ads X buttons
ads_folder = f"images/{res_set}/ads/x/"
ads_x = [cv2.imread(ads_folder + img_path) for img_path in os.listdir(ads_folder)]
ad_resumevideo_btn = cv2.imread(f"images/{res_set}/ads/ads_resumevideo_btn.PNG")
