from PIL import ImageGrab
import pyautogui;
import keyboard
import time

#I used https://pixspy.com/ for image cordinates and https://www.crazygames.com/game/perfect-piano for the game on 1920 X 1080
#Change the res values to capture the piano part
#Change abs_y to control the y value of the pixel being checked
#After running the program press Q to initiate it
#Hold T to terminate the program

res = [613, 0, 1307, 1079]
tiles_x = [88, 260, 433, 605]
abs_y = 883 #y value you want to check
abs_x = res[0] #x of the image
x_offset = 30 #offset if there is something in the middle of the note
y_offset = 0 #offset on y to click lower than the measurement cause the note moves
global screen;

def check():
    for x in tiles_x:
        pixel = screen.getpixel(xy = [x - x_offset, abs_y])
        if(pixel[0] < 60 and pixel[1] < 100 and pixel[2] < 100):
            pyautogui.mouseUp()
            pyautogui.moveTo(x + abs_x, abs_y + y_offset)
            pyautogui.mouseDown()
            break

while True:
    if(keyboard.is_pressed('q')):
        while True:
            screen = ImageGrab.grab(bbox=res)
            time.sleep(0.05)
            check()
            if(keyboard.is_pressed('t')):
                break
    if(keyboard.is_pressed('t')):
        break