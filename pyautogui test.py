import pyautogui

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
print(screenWidth, screenHeight)

Location = pyautogui.locateOnScreen('keg.png')  # returns (left, top, width, height) of first place it is found
print(Location)