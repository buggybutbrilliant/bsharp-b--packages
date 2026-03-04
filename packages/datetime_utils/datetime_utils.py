class ModuleObject:
    def __init__(self, name, exports):
        self.name = name
        self.exports = exports

def load():
    import datetime as _dt

    def _now():
        return _dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def _today():
        return _dt.date.today().strftime('%Y-%m-%d')

    def _year():
        return _dt.datetime.now().year

    def _month():
        return _dt.datetime.now().month

    def _day():
        return _dt.datetime.now().day

    def _hour():
        return _dt.datetime.now().hour

    def _minute():
        return _dt.datetime.now().minute

    def _weekday():
        days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        return days[_dt.datetime.now().weekday()]

    def _is_weekend():
        return _dt.datetime.now().weekday() >= 5

    def _format(date_str, fmt):
        try:
            d = _dt.datetime.strptime(str(date_str), '%Y-%m-%d')
            return d.strftime(str(fmt))
        except Exception as e:
            return f'ERROR: {e}'

    def _diff_days(date1, date2):
        try:
            d1 = _dt.datetime.strptime(str(date1), '%Y-%m-%d')
            d2 = _dt.datetime.strptime(str(date2), '%Y-%m-%d')
            return abs((d2 - d1).days)
        except Exception as e:
            return f'ERROR: {e}'

    def _add_days(date_str, n):
        try:
            d = _dt.datetime.strptime(str(date_str), '%Y-%m-%d')
            result = d + _dt.timedelta(days=int(n))
            return result.strftime('%Y-%m-%d')
        except Exception as e:
            return f'ERROR: {e}'

    return ModuleObject('datetime_utils', {
        'now':       _now,
        'today':     _today,
        'year':      _year,
        'month':     _month,
        'day':       _day,
        'hour':      _hour,
        'minute':    _minute,
        'weekday':   _weekday,
        'is_weekend': _is_weekend,
        'format':    _format,
        'diff_days': _diff_days,
        'add_days':  _add_days,
    })
