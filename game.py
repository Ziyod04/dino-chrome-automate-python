import pyautogui
from PIL import Image, ImageGrab
import time

def click(key):
    pyautogui.press(key)
    return

def isCollision(data):
 # Check colison for cactus
    for i in range(770, 860):
        for j in range(340, 370):
            if data[i, j] < 100:
                click("up")
                return


# Check colison for birds
    for i in range(770,800):
        for j in range(310, 337):
            if data[i, j] < 171:
                click("down")
                return
                

                
    return

if __name__ == "__main__":
    time.sleep(5)
    click('up') 
    
    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        isCollision(data)
        
        # # Draw the rectangle for cactus
        # for i in range(730, 810):
        #     for j in range(340, 370):
        #          data[i, j] = 0
        
        # # # Draw the rectangle for birds
        # for i in range(730, 760):
        #     for j in range(310, 335):
        #         data[i, j] = 171

        # image.show()
        # break