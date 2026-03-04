class ModuleObject:
    def __init__(self, name, exports):
        self.name = name
        self.exports = exports

def load():
    import math as _math

    def _clamp(value, mn, mx):
        return max(float(mn), min(float(mx), float(value)))

    def _lerp(a, b, t):
        return float(a) + (float(b) - float(a)) * float(t)

    def _sign(x):
        if float(x) > 0: return 1
        if float(x) < 0: return -1
        return 0

    def _degrees(radians):
        return _math.degrees(float(radians))

    def _radians(degrees):
        return _math.radians(float(degrees))

    def _is_even(n):
        return int(n) % 2 == 0

    def _is_odd(n):
        return int(n) % 2 != 0

    def _gcd(a, b):
        return _math.gcd(int(a), int(b))

    def _lcm(a, b):
        a, b = int(a), int(b)
        return abs(a * b) // _math.gcd(a, b)

    def _factorial(n):
        return _math.factorial(int(n))

    def _isPrime(n):
        n = int(n)
        if n < 2: return False
        for i in range(2, int(_math.sqrt(n)) + 1):
            if n % i == 0: return False
        return True

    return ModuleObject('math_extra', {
        'clamp':     _clamp,
        'lerp':      _lerp,
        'sign':      _sign,
        'degrees':   _degrees,
        'radians':   _radians,
        'is_even':   _is_even,
        'is_odd':    _is_odd,
        'gcd':       _gcd,
        'lcm':       _lcm,
        'factorial': _factorial,
        'is_prime':  _isPrime,
    })
