# flask-restplus-test

## Getting started
```python
$ virtualenv env
$ . env/bin/activate
$ pip install -r requirements_dev.txt
$ python api/api/app.py 
```

You can now visit `http://localhost:5000/api/1/` to see swagger documentation for v1 API.

v2 API is hosted under `http://localhost:5000/api/2/`, but entirely replaces v1 instead of adding to it.


Outstanding issues:
* Version fallback, v2 should expose /api/goodbye
  * Maybe just import v1 from v2 route definition...
* Route unit-testing
* Ability to set property for entire route family (e.g. login-required)
