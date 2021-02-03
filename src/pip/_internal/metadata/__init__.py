from pip._internal.utils.typing import MYPY_CHECK_RUNNING

if MYPY_CHECK_RUNNING:
    from typing import List, Optional

    from .base import BaseEnvironment


def get_default_environment():
    # type: () -> BaseEnvironment
    """Get the default representation for the current environment.

    This returns an Environment instance from the chosen backend. The default
    Environment instance should be built from ``sys.path`` and may use caching
    to share instance state accorss calls.
    """
    from .pkg_resources import Environment

    return Environment.default()


def get_environment(paths):
    # type: (Optional[List[str]]) -> BaseEnvironment
    """Get a representation of the environment specified by ``paths``.

    This returns an Environment instance from the chosen backend based on the
    given import paths. The backend must build a fresh instance representing
    the state of installed distributions when this function is called.
    """
    from .pkg_resources import Environment

    return Environment.from_paths(paths)
