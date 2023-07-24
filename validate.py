import os,sys

def get_path():
    if getattr(sys, 'frozen', False):
        main_path = os.path.dirname(sys.executable)
        return main_path
    elif __file__:
        main_path = os.path.dirname(__file__)
        return main_path

path = get_path()
txt_path = os.path.join(path,"switch.txt")
txt_exists = os.path.exists(txt_path)

if not txt_exists:
    print("Creted New File")
    file = open(txt_path,"w+")
    file.write("N")
    file.close()

def switch_status():
    file = open(txt_path, "r")
    status = file.read()
    file.close()
    return status

def update_status(self):
    file = open(txt_path, "w")
    file.write(self.upper())
    file.close()


