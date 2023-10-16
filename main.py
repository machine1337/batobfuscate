import argparse
from config import requirements, settings
from utils.banner import display_banner
from core.obfuscator import Obfuscator

def main():
    parser = argparse.ArgumentParser(description='Obfuscate a batch file.')
    parser.add_argument('file_path', type=str, help='Path of the batch file to obfuscate')
    args = parser.parse_args()

    requirements.install_requirements()
    display_banner()

    obfuscator = Obfuscator()
    success, error_code = obfuscator.obfuscate(args.file_path, method='Method1')
    if not success:
        print(f"Error Code: {error_code}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exited")
        exit()
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        exit(1)
