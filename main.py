import pyautogui
import time
import win32gui
import keyboard

def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

# App is process number; App name is the name of the process
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
    locate = pyautogui.locateCenterOnScreen('./images/{}_s.png'.format(btn_name), grayscale=False, confidence=0.5)
    locate = pyautogui.locateCenterOnScreen('./images/{}_m.png'.format(btn_name), grayscale=False, confidence=0.5)
    locate = pyautogui.locateCenterOnScreen('./images/{}_l.png'.format(btn_name), grayscale=False, confidence=0.5)
    return locate

def clickButton(btn_type):
    try:
        btn = locateButton(btn_type)
        pyautogui.moveTo(btn[0], btn[1])
        pyautogui.click()
    except TypeError:
        home_btn = locateButton("home")
        pyautogui.moveTo(home_btn[0], home_btn[1])
        pyautogui.click()
        if home_btn == None:
            print("Could not find Home Button. Closing App")
            quit()
        return
     
def gotoUniteFight():
    clickButton("uf")


def isLoading():
    return "hello"


def main():
    if __name__ == "__main__":
        print("GranBot v1.0.0")
        app = getProcess("granblue fantasy")
        if app == '':
            print("Granblue Fantasy is not open. Please open Granblue.")
            time.sleep(1)
            quit()

        focusWindow(app)
        print("Choice Menu:")
        print("1. Unite and Fight")
        print("2. Slime Blast")
        print("3. Angel Halo")
        print("4. Event")
        print(object)
        userInput = input()

        match userInput:
            case "1" : return gotoUniteFight()
         
        quit()
        
        # # pyautogui.click()
        # pyautogui.moveTo(location[0], location[1])
        # pyautogui.click()
    
main()