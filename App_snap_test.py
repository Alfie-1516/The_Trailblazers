import time

import pygetwindow as gw
from pywinauto import Desktop
import psutil
import pyautogui


def set_layout():
    all_data = []
    app_setting = []

    with open("output.txt", 'r', encoding='utf-8') as file:
        counter = 0
        for line in file:
            if ':' in line:
                app_setting.append(line.split(":")[1].strip())
            else:
                app_setting.append(line.strip())
            counter += 1
            if counter == 6:
                all_data.append(app_setting)
                app_setting = []
                counter = 0

    for apps in all_data:
        try:
            # Open the application using the start menu
            pyautogui.press('win')
            time.sleep(2)
            pyautogui.write(apps[0])
            time.sleep(2)
            pyautogui.press('enter')
            time.sleep(2)

            print(f"Attempting to position: {apps[0]}")
            app_exe = apps[0]
            # Get the window
            app_windows = gw.getWindowsWithTitle(app_exe)
            if not app_windows:
                print(f"Window with title '{apps[0]}' not found.")
                continue
            app_window = app_windows[0]
            new_left = int(apps[4])
            new_top = int(apps[5])
            new_width = int(apps[2])
            new_height = int(apps[3])

            # Resize and move the window
            app_window.resizeTo(new_width, new_height)
            time.sleep(2)
            app_window.moveTo(new_left, new_top)



        except Exception as e:
            print(f"An error occurred while processing {apps[0]}: {e}")

    return 0


def get_running_apps():
    desktop = Desktop(backend="uia")
    windows = desktop.windows()
    running_title = []
    running_exe = []
    apps = " "
    for window in windows:
        try:
            # Get the window title
            title = window.window_text()

            # Get the process ID (PID) of the window
            pid = window.process_id()

            # Get the process name (executable name) using psutil
            process = psutil.Process(pid)
            exe_name = process.name()

            if title and exe_name:
                apps = title.split(" - ")[-1] + "  " + exe_name

                running_title.append(str(exe_name))
                running_exe.append(title.split(" - ")[-1])
        except Exception as e:
            print(f"Error: {e}")
    return running_title, running_exe


def get_app_layout():
    title_application = ["OneNote", "Visual Studio Code", "Microsoft Edge"]
    application_exe = ["ONENOTE.EXE", "Code.exe", "msedge.exe"]

    # Ensure both lists have the same length
    if len(title_application) != len(application_exe):
        print("The length of title_application and application_exe must be the same.")
        return

    with open("output.txt", "w", encoding="utf-8") as f:
        for count, apps in enumerate(title_application):
            opened_windows = gw.getWindowsWithTitle(apps)
            if opened_windows:
                notepad = opened_windows[0]
                # Get the current width, height, and location
                width = notepad.width
                height = notepad.height
                left = notepad.left
                top = notepad.top

                result = f"{apps}\n exe: {application_exe[count]}\nWidth: {width}\nHeight: {height}\nLeft: {left}\nTop: {top}\n"

                # Print to console
                print(result)

                # Write to file
                f.write(result)
            else:
                print(f"Window with title '{apps}' not found.")




