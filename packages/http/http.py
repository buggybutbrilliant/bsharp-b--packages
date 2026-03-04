class ModuleObject:
    def __init__(self, name, exports):
        self.name = name
        self.exports = exports

def load():
    from urllib.request import urlopen, Request
    from urllib.error   import URLError, HTTPError
    import json as _json

    def _get(url):
        try:
            req = Request(str(url), headers={'User-Agent': 'bsharp-http/1.0'})
            with urlopen(req, timeout=15) as r:
                return r.read().decode('utf-8')
        except HTTPError as e:
            return f'ERROR: HTTP {e.code}'
        except URLError as e:
            return f'ERROR: {e.reason}'

    def _post(url, body):
        try:
            data = str(body).encode('utf-8')
            req  = Request(str(url), data=data, headers={
                'User-Agent':   'bsharp-http/1.0',
                'Content-Type': 'application/json'
            })
            with urlopen(req, timeout=15) as r:
                return r.read().decode('utf-8')
        except HTTPError as e:
            return f'ERROR: HTTP {e.code}'
        except URLError as e:
            return f'ERROR: {e.reason}'

    def _status(url):
        try:
            req = Request(str(url), headers={'User-Agent': 'bsharp-http/1.0'})
            with urlopen(req, timeout=15) as r:
                return r.status
        except HTTPError as e:
            return e.code
        except URLError:
            return 0

    def _parse(text):
        try:
            return _json.loads(str(text))
        except Exception:
            return None

    def _stringify(obj):
        try:
            return _json.dumps(obj)
        except Exception:
            return str(obj)

    return ModuleObject('http', {
        'get':       _get,
        'post':      _post,
        'status':    _status,
        'parse':     _parse,
        'stringify': _stringify,
    })
