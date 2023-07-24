from AppOpener import open,close
import os, sys
from validate import switch_status, update_status

status = switch_status().lower()

if status == "n":
    print("Status set to Neutral")
    code = False
if status == "c":
    print("Status set to Close")
    code = "close"
if status == "o":
    print("Status set to Open")
    code = "open"

while True:
    if not code:
        inp = input("N: ").strip()
        inp.replace("N: ","")
        if "close " in inp:
            app_name = inp.replace("close ", "").strip()
            close(app_name, match_closest=True)  # App will be close be it matches little bit too (Without printing context (like CLOSING <app_name>))
        if "open " in inp:
            app_name = inp.replace("open ", "")
            open(app_name, match_closest=True)  # App will be open be it matches little bit too
        if inp == "shutdown":
            os.system("shutdown /s /t 0")
        if "set " in inp:
            updated_status = inp.replace("set ","").lower()
            update_status(updated_status)

    if code == "close":
        inp = input("C: ").strip()
        inp.replace("C: ","")
        if inp == "shutdown":
            os.system("shutdown /s /t 0")
        if "set " in inp:
            updated_status = inp.replace("set ","").lower()
            update_status(updated_status)
        else:
            close(inp, match_closest=True)

    if code == "open":
        inp = input("O: ").strip()
        inp.replace("O: ","")
        if "set " in inp:
            updated_status = inp.replace("set ","").lower()
            update_status(updated_status)
        elif inp == "shutdown":
            os.system("shutdown /s /t 0")
        elif "set " in inp:
            updated_status = inp.replace("set ","").lower()
            update_status(updated_status)
        else:
            open(inp, match_closest=True)

