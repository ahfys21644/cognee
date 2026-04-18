"""Cognee - Knowledge graph and memory layer for AI applications."""

# Personal fork - added get_version() helper and noted config import for easy access
from cognee.api.v1.cognify import cognify
from cognee.api.v1.add import add
from cognee.api.v1.search import search
from cognee.api.v1.prune import prune
from cognee.config import Config

__version__ = "0.1.0"
__all__ = ["cognify", "add", "search", "prune", "Config", "get_version"]


def get_version() -> str:
    """Return the current version of cognee."""
    return __version__
