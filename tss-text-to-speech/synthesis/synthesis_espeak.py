import os
from subprocess import call

string = "Hello Python World!"
espeak_path = 'E:\eSpeak\command_line\espeak.exe'

# -------------------- [1] Method: Using os system.
# Documentation: http://espeak.sourceforge.net/commands.html
os.system(f'{espeak_path} -v en -s 140 {string}')

# -------------------- [2] Method: Using subprocess.
call([espeak_path, string])
