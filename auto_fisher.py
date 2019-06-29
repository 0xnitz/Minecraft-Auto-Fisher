from PIL import ImageGrab
from pynput.mouse import Listener, Button, Controller
import time

#Hello fellow programmer! My program is a little different version of kirb3's MC autofisher.
#This program measures the red pixels on rectangle given by the user and clicks the mouse if a fish is detected.
#To run this program open up minecraft and throw your fishing line into a body of water.
#Then, run the script and drag you mouse from the top left corner of the bobber to the bottom right (you don't need to be super accurate).
#Lastly, unpause the game and wait while the fish are coming to you! Have fun!
#-PreriKoth
clicks = []

def on_click(x, y, button, pressed): #This function gets called when a mouse click/release is performed
    if pressed: clicks.append((x,y))
    else: clicks.append((x,y))
    if not pressed: return False

print('Welcome to the Minecraft Auto Fisher.\nTo use this program please draw a rectangle on the minecraft fishing bobber by sliding the mouse from the top left corner to the bottom right one.')

with Listener( #This listens to mouse clicks until a False is returned
        on_click=on_click) as listener:
    listener.join()

print('Recieved scanning area!')
print(clicks)
rect = (clicks[0][0], clicks[0][1], clicks[1][0], clicks[1][1]) #After recieveing the rectangle scanning area we define the rectangle of measure.
last = 0
print('Starting to fish for you in 5 seconds, make sure you unpause Minecraft...')
time.sleep(5) #Giving the user time to unpause the game

while 1:
    im = ImageGrab.grab(rect) #screenshotting the rectangle given by the user every 1/3 of a second.
    redness = list(im.getdata(0)) #measuring the redness in the rectangle
    print('Pixel value: ' + str(round(sum(redness)/len(redness), 2)))
    
    if last != 0 and (sum(redness)/len(redness)) / last <= 0.7: #if the redness level is under .7 of the last measurement that means a fish has bitten.
        print('We got a fish people!')
        mouse = Controller()
        mouse.click(Button.right) #clicking the mouse to get the fish
        print('Resetting...')
        time.sleep(3)
        mouse.click(Button.right) #after 3 seconds throwing back the bobber into the water and resetting the program
        last = 0

    time.sleep(0.35)
    last = sum(redness)/len(redness) #the last redness measurement
