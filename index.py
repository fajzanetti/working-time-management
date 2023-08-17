import subprocess

command = f"gnome-terminal -e 'python3 switch.py'"

subprocess.run(command, shell=True)