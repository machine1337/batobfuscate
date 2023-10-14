import subprocess
from pathlib import Path
import random,string, os
import platform

print("[*] Checking Requirements Module")
if platform.system().startswith("Linux"):
    try:
        import termcolor
    except:
        os.system("python3 -m pip install termcolor -q -q -q")
        import termcolor
    try:
        from pyqcolor import *
    except:
        os.system("python3 -m pip install pyqcolor -q -q -q")
        from pyqcolor import *
    try:
        import colorama
        from colorama import Fore, Back, Style
    except ImportError:
        os.system("python3 -m pip install colorama -q -q -q")
        import colorama
        from colorama import Fore, Back, Style
    try:
        from tqdm import tqdm
    except:
        os.system("python3 -m pip install tqdm -q -q -q")
        from tqdm import tqdm
elif platform.system().startswith("Windows"):
    try:
        import termcolor
    except:
        os.system("python -m pip install termcolor -q -q -q")
        import termcolor
    try:
        from pyqcolor import *
    except:
        os.system("python -m pip install pyqcolor -q -q -q")
        from pyqcolor import *
    try:
        import colorama
        from colorama import Fore, Back, Style
    except ImportError:
        os.system("python -m pip install colorama -q -q -q")
        import colorama
        from colorama import Fore, Back, Style
    try:
        from tqdm import tqdm
    except:
        os.system("python -m pip install tqdm -q -q -q")
        from tqdm import tqdm
colorama.deinit()
banner = Center.XCenter("""
    ____       _____    _   _        ___  _     _____           ____     _____
   | __ )  __ |_   _|__| | | |      / _ \| |__ |  ___|   _ ___ / ___|__ |_   _|__
   |  _ \ / _  || |/ __| |_| |_____| | | |  _ \| |_ | | | / __| |   / _  || |/ _ \`
   | |_) | (_| || | (__|  _  |_____| |_| | |_) |  _|| |_| \__ \ |__| (_| || |  __/
   |____/ \__,_||_|\___|_| |_|      \___/|_ __/|_|   \__,_|___/\____\__,_||_|\___|
                            \n\n
""")
def os():
  iden = platform.system()
  if(iden == "Windows"):
    print("\033c")
    print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
    obfuscate2()
  else:
    print("\033c")
    print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
    obfuscate2()
def obfuscate2():
    S = 5
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=S))
    file = input(Fore.GREEN+"\nEnter Path Of BAT File:- ")
    out_hex = []
    out_hex.extend(["FF", "FE", "26", "63", "6C", "73", "0D", "0A", "FF", "FE", "0A", "0D"])
    with open(f'{file}','rb') as f:
            penis = f.read()
    out_hex.extend(['{:02X}'.format(b) for b in penis])
    with open(f'{ran}.bat', 'wb') as f:
        for i in out_hex:
            f.write(bytes.fromhex(i))
    path_to_file = f'{ran}.bat'
    path = Path(path_to_file)
    if path.is_file():
        print(termcolor.colored('\n[ ✔ ] File Obfuscated Success...', 'cyan'))
    else:
        print(termcolor.colored('\n[ X ] Error Occured! Plz Run again',
                                'red'))
def catc():
    try:
      os()
    except KeyboardInterrupt:
      print("\nYou Pressed The Exit Button!")
      quit()
catc()
