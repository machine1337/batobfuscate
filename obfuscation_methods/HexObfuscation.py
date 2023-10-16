from pathlib import Path
import random
import string
import termcolor

class HexObfuscation:
    def obfuscate(self, file_path):
        if not Path(file_path).exists():
            return False, "E102"

        try:
            S = 5
            ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=S))
            out_hex = ["FF", "FE", "26", "63", "6C", "73", "0D", "0A", "FF", "FE", "0A", "0D"]

            with open(file_path, 'rb') as f:
                content = f.read()
            out_hex.extend(['{:02X}'.format(b) for b in content])

            with open(f'{ran}.bat', 'wb') as f:
                for i in out_hex:
                    f.write(bytes.fromhex(i))

            if Path(f'{ran}.bat').is_file():
                print(termcolor.colored('\n[ ✔ ] File Obfuscated Successfully', 'cyan'))
                return True, None
            else:
                return False, "E103"

        except Exception as e:
            print(f"An error occurred: {e}")
            return False, "E103"
