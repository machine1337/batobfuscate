import importlib.util
import os

class Obfuscator:
    def __init__(self, obfuscation_methods):
        self.methods = {}
        for method_config in obfuscation_methods:
            method_name = method_config['name']
            module_path = os.path.join(os.path.dirname(__file__), '..', 'obfuscation_methods', f"{method_name}.py")
            
            if not os.path.exists(module_path):
                print(f"Warning: Method {method_name} not found.")
                continue

            spec = importlib.util.spec_from_file_location(method_name, module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            self.methods[method_name] = getattr(module, method_name)

    def obfuscate(self, file_content, **kwargs):
        results = []
        for method_name, method_instance in self.methods.items():
            method_args = kwargs.get(method_name, {}).get('args', {})
            
            obfuscation_method = self.methods.get(method_name, None)
            if obfuscation_method is None:
                return False, f"E101: {method_name} not found"

            obfuscator_instance = obfuscation_method()
            success, result_or_error = obfuscator_instance.obfuscate(file_content, **method_args)
            
            if not success:
                return False, result_or_error
            
            results.append(result_or_error)

        return True, results
