import os
import time
import subprocess
import shutil

def copy_to_startup():
    startup_folder = os.environ['APPDATA'] + '\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\'
    script_path = os.path.realpath(__file__)
    if script_path not in os.listdir(startup_folder):
        shutil.copy2(script_path, startup_folder)


def shutdown():
    subprocess.call(['shutdown', '/s'])

def check_time():
    while True:
        current_time = time.gmtime()
        if current_time.tm_hour == 21:
            shutdown()
        time.sleep(5)

# Check für Startup, Check für die Zeit ;D
if __name__ == '__main__':
    copy_to_startup()
    check_time()