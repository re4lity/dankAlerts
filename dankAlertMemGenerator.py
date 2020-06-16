import sys
from PIL import Image, ImageFont, ImageDraw  
if (len(sys.argv) < 2):
    print("Missing arguments")
    print("dankAlertMemGenerator.exe \"c:\\dankAlerts.jpg\"  \"Meme message...\"")
    print("See the examples in this file")
    input("Press Enter to continue...")

    sys.exit()

image = Image.open(sys.argv[1])
draw = ImageDraw.Draw(image)  
font = ImageFont.truetype("arial", 18, encoding="unic")
text = sys.argv[2]
draw.text((5, 5), text, font = font, align ="left")
image.show()  

# EXAMPLE IMAGE
# https://raw.githubusercontent.com/firstoctet/dankAlerts/master/dankAlerts.jpg

# EXAMPLE MESSAGE
"""
    Sysmon Process Create / EventID 1 

    UtcTime: 2017-04-28 22:08:22.025

    ProgramPathName: 
    C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe

    **************************************************************************
    If you trust this Program and don't want this alert, add the 
    ProgramPathName value to the following file.

    C:\\Windows\\dankAlerts\\Authorized-Programs.txt 
    or IF webCheck is enabled..
    https://dankAlerts.local/Authorized-Programs.htm
    **************************************************************************
"""