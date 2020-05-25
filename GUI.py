from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO

led = LED(10)
led2 = LED(9)
led3 = LED(11)

win = Tk()
win.title("LED TOGGLER")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

def ledToggle():
    if led.is_lit:
        led.off()
        ledButton["text"] = "Turn Green LED on"
    else:
        led.on()
        ledButton["text"] = "Turn Green LED off"
        led2.off()
        led3.off()

def redToggle():
    if led.is_lit:
        led2.off()
        ledButton2["text"] = "Turn Red LED on"
    else:
        led2.on()
        ledButton2["text"] = "Turn Red LED off"
        led.off()
        led3.off()


def blueToggle():
    if led.is_lit:
        led3.off()
        ledButton3["text"] = "Turn Blue LED on"
    else:
        led3.on()
        ledButton3["text"] = "Turn Blue LED off"
        led.off()
        led2.off()

def close():
    RPi.GPIO.cleanup()
    win.destroy()
    
ledButton = Button(win, text = 'Turn Green LED On', font = myFont, command = ledToggle, bg = 'green', height =1, width = 24)
ledButton.grid(row=0, column=1)

ledButton2 = Button(win, text = 'Turn Red LED On', font = myFont, command = redToggle, bg = 'red', height =1, width = 24)
ledButton2.grid(row=1, column=1)

ledButton3 = Button(win, text = 'Turn Blue LED On', font = myFont, command = blueToggle, bg = 'blue', height =1, width = 24)
ledButton3.grid(row=2, column=1)



exitButton = Button(win, text = 'Exit', font = myFont, command =close, bg = 'red', height = 1, width = 6)
exitButton.grid(row=3, column=1)

win.protocol("WM_DELETE_WINDOW", close)

win.mainloop()
