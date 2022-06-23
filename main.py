import pyautogui
import time
import win32gui
import keyboard

def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

def getProcess(app_name):
    app = ''
    top_windows = []
    win32gui.EnumWindows(windowEnumerationHandler, top_windows)
    for i in top_windows:
        if app_name in i[1].lower():
            app = i[0]            
            break
    return app

def focusWindow(app):
    win32gui.ShowWindow(app, 4)
    win32gui.SetForegroundWindow(app)

def locateButton(btn_name):
    suffix = ["_s", "_m", "_l"]
    locate = None
    for i in suffix:
        locate = pyautogui.locateCenterOnScreen('./images/{}{}.png'.format(btn_name,i), grayscale=False, confidence=0.9)
        if locate != None:
            return locate
    return None
    
def clickButton(btn_type):
    try:
        btn = locateButton(btn_type)
        pyautogui.moveTo(btn[0], btn[1])
        pyautogui.click()
        return True
    except TypeError:
        print("Could not find button/banner. Returning to Home.")
        time.sleep(1)
        home_btn = locateButton("home")
        pyautogui.moveTo(home_btn[0], home_btn[1])
        pyautogui.click()
        if home_btn == None:
            print("Could not find Home button. Closing App")
            time.sleep(1)
            quit()
        return False
     
def uniteFight():
    buttons = ["uf", "ufsolo", "ufplus"]
    success = None
    for i in buttons:
        success = clickButton(i)
        isLoading()
        if success == False:
            break


def isLoading():
    load = locateButton("loading")
    while load != None:
        load = locateButton("loading")
        print("Loading...")
    return

def main():
    if __name__ == "__main__":
        print("GranBot v1.0.0")
        print("Playing in Medium Window Size is recommended!")
        print("Please have Granblue on the Home page when using app.")
        app = getProcess("granblue fantasy")
        if app == '':
            print("Granblue Fantasy is not open. Please open Granblue.")
            time.sleep(1)
            quit()

        focusWindow(app)
        print("Choice Menu:")
        print("1. Unite and Fight Extreme+ Farm")
        print("2. Slime Blast")
        print("3. Angel Halo")
        print("4. Event")
        print("5. Quit")
        userInput = input()

        match userInput:
            case "1" : return uniteFight()
         
        quit()
    
main()