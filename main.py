import argparse
from pathlib import Path


from config import requirements, settings
requirements.install_requirements()

from utils.banner import display_banner
from core.obfuscator import Obfuscator
import termcolor


def main():
    parser = argparse.ArgumentParser(description="Batch file obfuscation utility.")
    parser.add_argument("file_path", type=str, help="Path to the batch file that needs to be obfuscated.")
    args = parser.parse_args()

    if not Path(args.file_path).exists():
        print("Operation failed with error code: E102")
        return

    display_banner()

    file_name = Path(args.file_path).name
    output_file_name = f"{settings.OUTPUT_PREFIX}{file_name}{settings.OUTPUT_SUFFIX}"
    output_file_path = Path(settings.OUTPUT_PATH, output_file_name)
    
    Path(settings.OUTPUT_PATH).mkdir(parents=True, exist_ok=True)
    
    with open(args.file_path, 'rb') as f:
        file_content = f.read()

    obfuscator = Obfuscator(settings.OBFUSCATION_METHODS)
    
    success, result_or_error = obfuscator.obfuscate(file_content)
    
    if success:
        final_output = b''.join(result_or_error)
        with open(output_file_path, 'wb') as f:
            f.write(final_output)
        print(termcolor.colored(f'\n[ ✔ ] File Obfuscated Successfully as {output_file_name}', 'cyan'))
    else:
        print(f"Operation failed with error code: {result_or_error}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation interrupted by the user.")
        exit(1)
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        exit(1)
