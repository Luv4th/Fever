import os
import subprocess
from colorama import Fore
from Util.configs.Helper.Design import designe, util, system
current_time = util()
username = os.getlogin()
sys = "System"
option_1 = "Network.py"
option_2 = "Discord.py"
config_folder = "Util"
title = Fore.LIGHTRED_EX + r"""             
                         ,''`.     ,''`.                        
                     ,.,'''  '`--- ._,,'|                             __     
                   ,'                   /                            / _|                         
              __.-'                    |                             | |_   ___ __   __  ___  _ __ 
           ''                ___   ___ |                             |  _| / _ \\ \ / / / _ \| '__|
         ,'                  \(|\ /|)/ |                             | |  |  __/ \ V / |  __/| |
        ,'                 _     _     `._                           |_|   \___|  \_/   \___||_|          
       /     ,.......-\    `.      __     `-.                          
      /     ,' :  .:''`|    `:`.../:.`` ._   `._                       
  ,..,'  _/' .: :'     |     |      '.    \.    \                      
 /      ,'  :'.:  / \  |     | / \   ':.  . \    \                    
|      /  .: :' ,'  _)  ".._,;'  _)    :. :. \    |                  | 1 |  network related tools 
 |     | :'.:  /   |   .,   /   |       :  :  |   |                   
 |     |:' :  /____|  /  \ /____|       :  :  |  ,'                   
  |   /    '         /    \            :'   : |,/                     
   \ |  '_          /______\              , : |                       
  _/ |  \'`--`.    _            ,_   ,-'''  :.|         __            
 /   |   \..   ` ./ `.   _,_  ,'  ``'  /'   :'|      _,''/           
/   /'. :   \.   _    [_]   `[_]  .__,,|   _....,--=/'  /:           | 2 |  discord related tools
|   \_| :    `.-' `.    _.._     /     . ,'  :. ':/'  /'  `.         
`.   '`'`.         `. ,.'   ` .,'     :'/ ':..':.    |  .:' `.       
  \.      \          '               :' |    ''''      ''     `.     
    `''.   `|        ':     .      .:' ,|         .  ..':.      |    
      /'   / '"-..._  :   .:'    _;:.,'  \.     .:'   :. ''.    |    
     (._,.'        '`''''''''''''          \.._.:      ':  ':   /    
                                            '`- ._    ,:__,,-'       
"""

print(title)
gateway = input(designe(current_time, username ) + Fore.LIGHTWHITE_EX + "Select An Option : ")
if gateway == "1":
    os.chdir(config_folder)
    subprocess.run(["python", option_1])
elif gateway == "2":
    os.chdir(config_folder)
    subprocess.run(["python", option_2])
else:
    print (system(current_time, sys)+ "Invalid option! Please select 1, 2, or 3.")
    input(
        system(current_time, sys) + "Press Enter to exit...")