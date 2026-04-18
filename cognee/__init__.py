"""Cognee - Knowledge graph and memory layer for AI applications."""

# Personal fork - added get_version() helper and noted config import for easy access
# Also added get_version_tuple() for easier version comparisons
# Note: search() defaults to SIMILARITY mode - may want to try GRAPH mode for some use cases
from cognee.api.v1.cognify import cognify
from cognee.api.v1.add import add
from cognee.api.v1.search import search
from cognee.api.v1.prune import prune
from cognee.config import Config

__version__ = "0.1.0"
__author__ = "topoteretes (fork)"
__all__ = ["cognify", "add", "search", "prune", "Config", "get_version", "get_version_tuple", "search_graph"]


def get_version() -> str:
    """Return the current version of cognee."""
    return __version__


def get_version_tuple() -> tuple:
    """Return the current version as a tuple of ints, e.g. (0, 1, 0).

    Useful for version comparisons:
        if get_version_tuple() >= (0, 1, 0):
            ...
    """
    return tuple(int(x) for x in __version__.split("."))


# TODO: explore wrapping search() with a helper that defaults to GRAPH mode,
# since SIMILARITY mode misses some relational context in my test datasets.
def search_graph(query: str, top_k: int = 10, **kwargs):
    """Convenience wrapper around search() using GRAPH mode by default.

    Added top_k param (default 10) since the default felt too low for my datasets.
    """
    from cognee.api.v1.search import SearchType
    return search(query, search_type=SearchType.GRAPH, top_k=top_k, **kwargs)
