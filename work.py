import pyautogui
import time
import random
from datetime import datetime
pyautogui.FAILSAFE = False
move = (0, 0)
count = 0
g_count = random.randint(2, 4) * -1
window = 0
now_org = datetime.now()
org_day = now_org.day
ini_min = random.randint(5, 55)
end_min = random.randint(5, 55)
max_m = 10
print(str(ini_min)+" "+str(end_min)+" "+str(max_m)+" min day")
while True:
    now = datetime.now()
    if (org_day != now.day):
        ini_min = random.randint(5, 55)
        end_min = random.randint(5, 55)
        org_day = now.day
        print(str(datetime.now())+" reset day")
        print(str(ini_min)+" "+str(end_min)+" "+str(max_m)+" min day")
    time.sleep(1)
    if (move == pyautogui.position()):
        count = count + 1
        #print(str(datetime.now())+" c "+str(count)+" "+str(g_count))
    else:
        move = pyautogui.position()
        count = 0
        g_count = 0
        window = 0
    if(count > max_m):
        count = 0
        if(now.hour != 14 and (now.hour > 7 or (now.minute > ini_min and now.hour > 6)) and (now.hour < 19 or (now.minute < end_min and now.hour < 22))):
            g_count = g_count + 1
            print(str(datetime.now())+" moving "+str(max_m)+" g_count "+str(g_count)+" window "+str(window))
            max_m = random.randint(100, 170)
            print("New max "+str(max_m))
            for i in range(0, random.randint(40, 60)):
                pyautogui.moveTo(random.randint(4, 6), i*random.randint(4, 6))
            for i in range(0, random.randint(2, 4)):
                pyautogui.press('shift')
            if g_count > 0:
                g_count = random.randint(2, 4) * -1
                window = window + 1
                pyautogui.keyDown('alt')
                time.sleep(1)
                for i in range(0, window):
                    pyautogui.press('tab')
                time.sleep(1)
                pyautogui.keyUp('alt')
                pyautogui.moveTo(0, 0)
                time.sleep(1)
                pyautogui.click()
                print(str(datetime.now())+" window g_count "+str(g_count)+" window "+str(window))
            move = pyautogui.position()
