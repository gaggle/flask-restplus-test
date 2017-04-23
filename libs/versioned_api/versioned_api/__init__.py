from flask_restplus import Api as _Api
from importlib import import_module as _import_module
from logging import getLogger as _getLogger

_log = _getLogger(__name__)


class BlueprintAttributeError(Exception):
    def __init__(self, path, name):
        super(BlueprintAttributeError, self).__init__(
            "Module '{}' does not expose blueprint variable '{}'".format(path, name))


def Api(app, versions=None, **kwargs):
    if versions is None:
        versions = {}

    # TODO: Sort items(), so numbers or alphabetically flows correctly
    for ver, module_path in versions.items():
        try:
            module_path, blueprint_var = module_path.rsplit(":", 1)
        except ValueError:
            blueprint_var = 'api'

        _log.info("Registering '%s' as version '%s'", module_path, ver)

        mod = _import_module(module_path, package=None)
        try:
            bp = getattr(mod, blueprint_var)
        except AttributeError:
            raise BlueprintAttributeError(module_path, blueprint_var)

        app.register_blueprint(bp, url_prefix='/api/{}'.format(ver))
    return _Api(app, **kwargs)
