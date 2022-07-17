import autoit
import time

autoit.run("notepad.exe")
autoit.win_wait_active("[CLASS:Notepad]", 3)
time.sleep(1)
autoit.control_send("[CLASS:Notepad]", "Edit", "hello world{!}")
autoit.win_close("[CLASS:Notepad]")
autoit.control_click("[Class:#32770]", "Button2")