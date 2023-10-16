from obfuscation_methods import HexObfuscation

class Obfuscator:
    def __init__(self):
        self.methods = {
            "HexObfuscation": HexObfuscation
        }

    def obfuscate(self, file_path, method="HexObfuscation", **kwargs):
        obfuscation_method = self.methods.get(method, None)
        if obfuscation_method is None:
            return False, "E101"

        obfuscator_instance = obfuscation_method()
        return obfuscator_instance.obfuscate(file_path, **kwargs)
