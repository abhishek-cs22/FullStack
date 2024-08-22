import pyautogui
import time

count = 0
while (count <= 50):
    pyautogui.typewrite("bheja fry ho gya hai tera")
    pyautogui.press('enter')  # Press enter to send the message
    count += 1
    time.sleep(0) # Add a delay to avoid potential issues