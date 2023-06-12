import subprocess
import time
import pytesseract
from PIL import Image
phone_numbers = []
for i in range(50):
    number = "98684500{:02d}".format(i)
    phone_numbers.append(number)
output_file = "profile_names.txt"  
with open(output_file, 'w') as f:
    for number in phone_numbers:
        subprocess.run(['adb', 'shell', 'input', 'text', number])
        time.sleep(0.5)
        subprocess.run(['adb', 'shell', 'input', 'tap', '558', '1307'])
        time.sleep(0.5)
        screenshot_path = "truecaller_ss/{0}.png".format(number)
        subprocess.run(['adb', 'shell', 'screencap', '/sdcard/screenshot.png'])
        subprocess.run(['adb', 'pull', '/sdcard/screenshot.png', screenshot_path])
        profile_name = pytesseract.image_to_string(Image.open(screenshot_path).crop((1,527,1073,612)))
        f.write(number + ": " + profile_name.strip() + '\n')
        subprocess.run(['adb', 'shell', 'input', 'tap', '71', '175'])
        time.sleep(0.5)
        subprocess.run(['adb', 'shell', 'input', 'tap', '810', '196'])
print("Profile names saved to:", output_file)