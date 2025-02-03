import os
sys = "System"
from Util.configs.Helper.Design import system, util
username, current_time = util()
os.system("python -m pip install -r requirements.txt")
input(system(current_time, sys) + "Press Enter to exit...")