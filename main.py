import pyautogui
import time
import win32gui
import autoit

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
    locate = pyautogui.locateCenterOnScreen(f'./images/{btn_name}.png', grayscale=False, confidence=0.9)
    if locate != None:
        return locate
    return None
    
def clickButton(btn_type):
    try:
        btn = locateButton(btn_type)
        pyautogui.click(btn[0], btn[1])
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

def isDisabled():
    disabled = locateButton("disabled")
    while disabled != None:
        print(disabled)
        disabled = locateButton("disabled") 
         

def farmDungeon():
    input("Run a dungeon and then leave it on Quest Result page. Press Enter when ready.")
    clickButton("playagain")
    isLoading()
    time.sleep(1)
    pyautogui.click()
    time.sleep(0.5)
    clickButton("ok")
    isLoading()
    isDisabled()

    

def main():
    if __name__ == "__main__":
        print("GranBot v1.0.0")
        print("Remember to play on medium window size!")
        app = getProcess("granblue fantasy")
        if app == '':
            print("Granblue Fantasy is not open. Please open Granblue.")
            time.sleep(1)
            quit()

        focusWindow(app)
        print("Choice Menu:")
        print("1. Unite and Fight Extreme+ Farm")
        userInput = input()

        match userInput:
            case "1" : return farmDungeon()
        quit()
    
main()