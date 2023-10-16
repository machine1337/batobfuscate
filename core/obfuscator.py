from obfuscation_methods import BaseMethod, Method1

class Obfuscator:
    def __init__(self):
        self.methods = {
            'Method1': Method1
        }

    def obfuscate(self, file_path, method):
        obfuscation_method = self.methods.get(method)
        if obfuscation_method is None:
            return False, "E101"

        obfuscator = obfuscation_method()
        return obfuscator.obfuscate(file_path)
