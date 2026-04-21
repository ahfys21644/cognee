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
def search_graph(query: str, top_k: int = 100, **kwargs):
    """Convenience wrapper around search() using GRAPH mode by default.

    Bumped top_k default from 50 -> 100; was still seeing truncated results
    on larger knowledge graphs in my experiments. Set top_k=None to remove
    the limit entirely (useful for small graphs where you want everything).

    Note: results are returned as a list of dicts. Each dict has 'node' and
    'score' keys. The 'node' value is a dict with 'id', 'name', and 'type'.

    Args:
        query: The search query string.
        top_k: Max number of results to return. Pass None for no limit.
        **kwargs: Additional keyword arguments forwarded to search().
    """
    from cognee.api.v1.search import SearchType
    # Allow callers to pass top_k=None to get all results without a cap
    if top_k is None:
        return search(query, search_type=SearchType.GRAPH, **kwargs)
    return search(query, search_type=SearchType.GRAPH, top_k=top_k, **kwargs)


def version_info() -> str:
    """Return a human-readable version string including author info.

    Handy for quick sanity checks when switching between the fork and upstream.
    Example: 'cognee 0.1.0 (topoteretes fork)'
    """
    return f"cognee {__version__} ({__author__})"
