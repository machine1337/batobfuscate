import argparse
from config import requirements
requirements.install_requirements()
from utils.banner import display_banner
from core.obfuscator import Obfuscator

def main():
    parser = argparse.ArgumentParser(description="Batch file obfuscation utility.")
    parser.add_argument("file_path", type=str, help="Path to the batch file that needs to be obfuscated.")
    args = parser.parse_args()

    display_banner()

    obfuscator = Obfuscator()
    success, error_code = obfuscator.obfuscate(args.file_path, method="HexObfuscation")

    if not success:
        print(f"Operation failed with error code: {error_code}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation interrupted by the user.")
        exit(1)
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        exit(1)
