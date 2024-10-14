import pyautogui as pg
import time
import pytesseract as ra
buff=10
duration=0.18
lastleft=0
lastright=0
tm=time.time()
pg.click(819,764,duration=0)
while time.time()-tm<20:
    region=(780,318,1098-780,433-318)
    ar=pg.screenshot('a.png',region=region)
    config = r'-l chi_sim+eng --psm 6'
    a=ra.image_to_string(ar,config=config)
    left=0
    right=0
    
    state=0
    for i in a:
        if i.isdigit():
            if state==0:
                left=int(i)
                state=1
            elif state==1:
                left=left*10+int(i)
            elif state==2:
                right=int(i)
                state=3
            elif state==3:
                right=right*10+int(i)
            else:
                left=0
                right=0
                break
        else:
            if state==1:
                state=2
            elif state==3:
                state=4
    
    if (left==0 or right==0) or (left>20 or right>20):
        continue
    print(left,right)
    if left>right:
        pg.press('right')
    elif left<right:
        pg.press('left')
    else:
        pg.press('up')
    time.sleep(0.38)
