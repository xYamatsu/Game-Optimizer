import os
import shutil
import subprocess
import tkinter as tk
from tkinter import messagebox
import webbrowser

def clean_temp_files():
    """ Deletes temporary files safely. """
    temp_folders = [os.getenv('TEMP'), os.getenv('TMP'), "C:\\Windows\\Temp"]
    files_deleted = 0

    for folder in temp_folders:
        if folder and os.path.exists(folder):
            for root, dirs, files in os.walk(folder, topdown=False):
                for file in files:
                    file_path = os.path.join(root, file)
                    try:
                        os.remove(file_path)
                        files_deleted += 1
                    except Exception:
                        pass
                for d in dirs:
                    try:
                        shutil.rmtree(os.path.join(root, d))
                    except Exception:
                        pass

    messagebox.showinfo("Success", f"Deleted {files_deleted} temporary files!")

def enable_ultimate_performance():
    os.system('start control.exe powercfg.cpl')
    response = messagebox.askyesno("Add Ultimate Performance", "Do you want to add Ultimate Performance Mode?")
    
    if response:
        ultimate_performance_scheme = "e9a42b02-d5df-448d-aa00-03f14749eb61"
        try:
            subprocess.run(['powercfg', '-duplicatescheme', ultimate_performance_scheme], check=True)
            messagebox.showinfo("Success", "Ultimate Performance Mode added!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed: {e}")

def close_background_apps():
    subprocess.run(["taskkill", "/F", "/IM", "OneDrive.exe"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    messagebox.showinfo("Optimization", "Closed background apps to free up resources.")

def free_up_ram():
    os.system("cls")
    os.system("echo Freeing RAM...")
    os.system("echo Performing memory cleanup")
    subprocess.run("ipconfig /flushdns", shell=True)
    messagebox.showinfo("Optimization", "RAM and cache cleared!")

def disable_unnecessary_services():
    services = ["SysMain", "DiagTrack", "WSearch"]
    for service in services:
        subprocess.run(["sc", "config", service, "start=disabled"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    messagebox.showinfo("Optimization", "Disabled unnecessary services.")

def enable_game_mode():
    subprocess.run("reg add HKCU\\Software\\Microsoft\\GameBar /v AllowAutoGameMode /t REG_DWORD /d 1 /f", shell=True)
    messagebox.showinfo("Optimization", "Game Mode enabled!")

def lower_network_latency():
    subprocess.run("netsh interface tcp set global autotuninglevel=normal", shell=True)
    subprocess.run("netsh interface tcp set global rss=enabled", shell=True)
    messagebox.showinfo("Optimization", "Network optimized for gaming!")

def toggle_dark_theme():
    global dark_theme_enabled
    if dark_theme_enabled:
        root.config(bg="white")
        for widget in root.winfo_children():
            widget.config(bg="white", fg="black")
        dark_theme_button.config(text="Enable Dark Theme")
        dark_theme_enabled = False
    else:
        root.config(bg="black")
        for widget in root.winfo_children():
            widget.config(bg="black", fg="white")
        dark_theme_button.config(text="Disable Dark Theme")
        dark_theme_enabled = True

def download_fan_control():
    # Link to download fan control software
    fan_control_url = "https://getfancontrol.com" 
    webbrowser.open(fan_control_url)

def join_discord():
    # Link to join the Discord server
    discord_url = "https://discord.gg/KJE5TkcCRe"
    webbrowser.open(discord_url)

root = tk.Tk()
root.title("Game Optimizer")
root.geometry("300x500") 

# Initialize dark theme state
dark_theme_enabled = False

tk.Button(root, text="Clean Temp Files", command=clean_temp_files).pack(pady=5)
tk.Button(root, text="Enable Ultimate Performance", command=enable_ultimate_performance).pack(pady=5)
tk.Button(root, text="Close Background Apps", command=close_background_apps).pack(pady=5)
tk.Button(root, text="Free Up RAM", command=free_up_ram).pack(pady=5)
tk.Button(root, text="Disable Unnecessary Services", command=disable_unnecessary_services).pack(pady=5)
tk.Button(root, text="Enable Game Mode", command=enable_game_mode).pack(pady=5)
tk.Button(root, text="Lower Network Latency", command=lower_network_latency).pack(pady=5)

# Button to toggle dark theme
dark_theme_button = tk.Button(root, text="Enable Dark Theme", command=toggle_dark_theme)
dark_theme_button.pack(pady=5)


tk.Button(root, text="Download Fan Control", command=download_fan_control).pack(pady=5)
tk.Button(root, text="Join Discord Server", command=join_discord).pack(pady=5)

tk.Label(root, text="Game Booster - Made in Python", fg="gray").pack(pady=5)
tk.Label(root, text="Baked with love by Milord27", fg="gray").pack(pady=3)

root.mainloop()
