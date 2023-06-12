import subprocess
import time
import pytesseract
from PIL import Image

phone_numbers = []
for i in range(10):
    number = "98684500{:02d}".format(i)
    phone_numbers.append(number)

for number in phone_numbers:
    subprocess.run(['adb', 'shell', 'input', 'text', number])
    time.sleep(1)
    subprocess.run(['adb', 'shell', 'input', 'tap', '558', '1307'])
    time.sleep(1)
    screenshot_path = "/Users/tazer/Desktop/truecaller_ss/{0}.png".format(number)
    subprocess.run(['adb', 'shell', 'screencap', '/sdcard/screenshot.png'])
    subprocess.run(['adb', 'pull', '/sdcard/screenshot.png', screenshot_path])
    print("Screenshot saved:", screenshot_path)
    profile_name = pytesseract.image_to_string(Image.open(screenshot_path).crop((1,527,1073,612)))
    print("Profile Name:", profile_name)
    subprocess.run(['adb', 'shell', 'input', 'tap', '71', '175'])
    time.sleep(1)
    subprocess.run(['adb', 'shell', 'input', 'tap', '810', '196'])
