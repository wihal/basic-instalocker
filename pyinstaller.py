import subprocess

# This code is for automating the pyinstaller process
pyinstaller_path = r"C:\Users\willi\AppData\Roaming\Python\Python311\Scripts\pyinstaller.exe"
main_script = r"C:\Users\willi\Desktop\valo\main.pyw"
output_folder = r"C:\Users\willi\Desktop\valo\output"
icon = r"C:\Users\willi\Desktop\valo\.vlocker\icon.ico"

pyinstaller_command = [
    pyinstaller_path,
    main_script,
    "--noconfirm",
    "--onefile",
    "--windowed",
    "--icon", icon,
    "--distpath", output_folder,
    '--name', 'Vlocker',
    '--add-data', "C:/Users/willi/Desktop/valo/brain.py;.",
    '--add-data', "C:/Users/willi/Desktop/valo/agent_manager.py;."
]

subprocess.run(pyinstaller_command)

subprocess.run(r'"C:\Program Files (x86)\Inno Setup 6\Compil32.exe" Installer.iss', shell=True)
