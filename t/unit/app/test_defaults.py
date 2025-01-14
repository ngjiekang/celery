import sys
from importlib import import_module

from celery.app.defaults import (
    _OLD_DEFAULTS,
    _OLD_SETTING_KEYS,
    _TO_NEW_KEY,
    _TO_OLD_KEY,
    DEFAULTS,
    NAMESPACES,
    SETTING_KEYS,
)


class test_defaults:
    def setup(self):
        self._prev = sys.modules.pop("celery.app.defaults", None)

    def teardown(self):
        if self._prev:
            sys.modules["celery.app.defaults"] = self._prev

    def test_option_repr(self):
        assert repr(NAMESPACES["broker"]["url"])

    def test_any(self):
        val = object()
        assert self.defaults.Option.typemap["any"](val) is val

    def test_compat_indices(self):
        assert not any(key.isupper() for key in DEFAULTS)
        assert not any(key.islower() for key in _OLD_DEFAULTS)
        assert not any(key.isupper() for key in _TO_OLD_KEY)
        assert not any(key.islower() for key in _TO_NEW_KEY)
        assert not any(key.isupper() for key in SETTING_KEYS)
        assert not any(key.islower() for key in _OLD_SETTING_KEYS)
        assert not any(value.isupper() for value in _TO_NEW_KEY.values())
        assert not any(value.islower() for value in _TO_OLD_KEY.values())

        for key in _TO_NEW_KEY:
            assert key in _OLD_SETTING_KEYS
        for key in _TO_OLD_KEY:
            assert key in SETTING_KEYS

    def test_find(self):
        find = self.defaults.find

        assert find("default_queue")[2].default == "celery"
        assert find("task_default_exchange")[2] is None

    @property
    def defaults(self):
        return import_module("celery.app.defaults")
