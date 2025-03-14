🎮 Game Optimizer 🖥️
Welcome to Game Optimizer - the ultimate tool to boost your PC's performance with just a click! This Python-powered app will help you optimize your system for gaming by cleaning up junk files, enabling high-performance modes, freeing up RAM, and more! 🏎️💨

📜 Features:
Clean Temp Files: 🧹
Deletes temporary files and directories from your system to free up precious disk space. We use shutil.rmtree() for safely removing files and directories.

Enable Ultimate Performance: ⚡
Activate Ultimate Performance Mode to maximize system resources. This feature directly interacts with Windows' power settings to push your system into overdrive.

Close Background Apps: 🚫
Close resource-heavy apps running in the background, like OneDrive, to free up your system’s memory for more critical tasks (like gaming!).

Free Up RAM: 🧠
Flush your DNS cache and clear up system RAM, enhancing your PC's responsiveness and performance.

Disable Unnecessary Services: ⚙️
Disable unnecessary background services like SysMain and WSearch that can slow down your system.

Enable Game Mode: 🎮
Automatically enable Game Mode in Windows to prioritize gaming resources and reduce interruptions from system processes.

Lower Network Latency: 🌐
Fine-tune your network settings to reduce lag while gaming by tweaking TCP settings for smoother online gameplay.

Toggle Dark Theme: 🌑
Switch between light and dark themes for the app interface. Keep your workspace comfy and stylish!

Download Fan Control Software: 🌀
Want to keep your system cool while gaming? Download fan control software with a single click!

Join Discord Server: 💬
Join our gaming community on Discord for tips, updates, and to connect with fellow gamers.

🛠️ Tech Stack:
Python 3: The core language for building this tool.
Tkinter: Used for the beautiful GUI to keep things simple and interactive.
shutil.rmtree: Used to delete files and directories safely.
subprocess: Manages system-level commands and scripts to execute optimizations.
webbrowser: Opens external links (such as the Discord server and download links).
Messagebox: For displaying useful notifications and alerts in a user-friendly way.
🚀 How It Works:
Temporary File Cleanup:
The app searches for system temp files using os.walk and deletes them one by one using os.remove and shutil.rmtree. By doing so, it ensures that not only individual files but also any temporary folders are cleaned.

Ultimate Performance Mode:
This is achieved by calling powercfg via subprocess.run. If the user wants to activate it, the app duplicates the Ultimate Performance power scheme into their system, unlocking maximum resource usage for high-performance tasks.

Game Mode and Network Latency:
Tweaks like modifying Windows' registry for Game Mode and adjusting network settings are done with simple command line operations executed using subprocess. These commands improve the user’s gaming experience by lowering background noise and optimizing network conditions.

Dark Mode:
The app uses Tkinter to change the theme dynamically. It updates the background color of the main window and all child widgets to create an immersive dark or light experience, depending on the user’s preference.



Click on the buttons to activate each optimization feature.
Enjoy a smoother, faster gaming experience!

📢 Contribute:
We'd love your contributions! If you have an idea to make this tool even better, feel free to open a pull request. Let's make gaming more efficient together! 🎮💪

📚 Learn More:
Tkinter Docs: https://docs.python.org/3/library/tkinter.html
shutil.rmtree: https://docs.python.org/3/library/shutil.html#shutil.rmtree
⚡ Made with Love ❤️ by Milord27
Stay awesome, stay optimized! 💻🎮

