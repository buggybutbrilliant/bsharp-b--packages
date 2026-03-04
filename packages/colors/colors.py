class ModuleObject:
    def __init__(self, name, exports):
        self.name = name
        self.exports = exports

def load():
    def _red(text):     print(f'\033[31m{text}\033[0m'); return None
    def _green(text):   print(f'\033[32m{text}\033[0m'); return None
    def _yellow(text):  print(f'\033[33m{text}\033[0m'); return None
    def _blue(text):    print(f'\033[34m{text}\033[0m'); return None
    def _cyan(text):    print(f'\033[36m{text}\033[0m'); return None
    def _magenta(text): print(f'\033[35m{text}\033[0m'); return None
    def _bold(text):    print(f'\033[1m{text}\033[0m');  return None
    def _reset(text):   print(f'\033[0m{text}\033[0m');  return None

    return ModuleObject('colors', {
        'red':     _red,
        'green':   _green,
        'yellow':  _yellow,
        'blue':    _blue,
        'cyan':    _cyan,
        'magenta': _magenta,
        'bold':    _bold,
        'reset':   _reset,
    })
