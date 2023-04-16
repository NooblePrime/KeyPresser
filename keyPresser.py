import PySimpleGUI as sg
from time import sleep
from pynput.mouse import Button, Controller
from pynput import keyboard
import threading
clicking = False
cps = 1000

def press_callback(key):
    global clicking
    if key == keyboard.Key.f6:
        clicking = not clicking
        if clicking == True:
            thread = threading.Thread(target = clicker)
            thread.start()

keyList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
            "shift", "tab", "enter", "space", "backspace", "leftMB", "rightMB"]

def clicker():
        global clicking
        global values
        if values[1] == "leftMB":
            while clicking == True:
                Controller().click(Button.left, 1)
                sleep(1/cps)
        elif values[1] == "rightMB":
            while clicking == True:
                Controller().click(Button.right, 1)
                sleep(1/cps)
        elif values[1] == "shift":
            while clicking == True:
                keyboard.Controller().tap(keyboard.Key.shift)
                sleep(1/cps)
        elif values[1] == "tab":
            while clicking == True:
                keyboard.Controller().tap(keyboard.Key.tab)
                sleep(1/cps)
        elif values[1] == "enter":
            while clicking == True:
                keyboard.Controller().tap(keyboard.Key.enter)
                sleep(1/cps)
        elif values[1] == "space":
            while clicking == True:
                keyboard.Controller().tap(keyboard.Key.space)
                sleep(1/cps)
        elif values[1] == "backspace":
            while clicking == True:
                keyboard.Controller().tap(keyboard.Key.backspace)
                sleep(1/cps)
        else:
            while clicking == True:
                keyboard.Controller().tap(keyboard.KeyCode.from_char(values[1]))
                sleep(1/cps)

layout = [
    [sg.Text("Enter presses per second. If nothing, a letter or a number above 1000 is entered, will default to 1000.\nPress Submit to enter a new value and F6 to start or stop pressing.")],
    [sg.Text('Presses per second:', size =(15, 1)), sg.InputText()],
    [sg.Text("Button to press:"), sg.Combo(keyList, enable_events=True, readonly=True, default_value=keyList[0])],
    [sg.Submit()]]

window = sg.Window("Nooble's Key Presser", layout)
listen = keyboard.Listener(on_press=press_callback)
listen.start()
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        listen.stop()
        break
    if event == "Submit":
        if values[0].isnumeric() and int(values[0]) <= 1000 and values[0] != '':
            cps = int(values[0])
        else:
            cps = 1000
