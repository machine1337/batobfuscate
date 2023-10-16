from pyqcolor import Colorate, Colors

def display_banner():
    banner_text = """
    [ Your Banner Here ]
    """
    print(Colorate.Vertical(Colors.green_to_yellow, banner_text, 2))
