"""Configuration management for cognee.

Loads settings from environment variables with sensible defaults.
"""

import os
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class CogneeConfig:
    """Central configuration object for the cognee library."""

    # LLM settings
    llm_provider: str = field(default_factory=lambda: os.getenv("LLM_PROVIDER", "openai"))
    llm_model: str = field(default_factory=lambda: os.getenv("LLM_MODEL", "gpt-4o-mini"))
    llm_api_key: Optional[str] = field(default_factory=lambda: os.getenv("LLM_API_KEY"))
    llm_api_base: Optional[str] = field(default_factory=lambda: os.getenv("LLM_API_BASE"))
    llm_temperature: float = field(
        # Keeping temperature at 0.0 for deterministic outputs — I prefer consistency
        default_factory=lambda: float(os.getenv("LLM_TEMPERATURE", "0.0"))
    )

    # Embedding settings
    embedding_provider: str = field(
        default_factory=lambda: os.getenv("EMBEDDING_PROVIDER", "openai")
    )
    embedding_model: str = field(
        default_factory=lambda: os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")
    )
    # Using 1536 dims for text-embedding-3-small; switch to 3072 if upgrading to text-embedding-3-large
    embedding_dimensions: int = field(
        default_factory=lambda: int(os.getenv("EMBEDDING_DIMENSIONS", "1536"))
    )

    # Vector store settings
    vector_db_provider: str = field(
        default_factory=lambda: os.getenv("VECTOR_DB_PROVIDER", "lancedb")
    )
    vector_db_url: Optional[str] = field(default_factory=lambda: os.getenv("VECTOR_DB_URL"))
    vector_db_key: Optional[str] = field(default_factory=lambda: os.getenv("VECTOR_DB_KEY"))

    # Graph store settings
    graph_db_provider: str = field(
        default_factory=lambda: os.getenv("GRAPH_DB_PROVIDER", "networkx")
    )
    graph_db_url: Optional[str] = field(default_factory=lambda: os.getenv("GRAPH_DB_URL"))
    graph_db_username: Optional[str] = field(
        default_factory=lambda: os.getenv("GRAPH_DB_USERNAME")
    )
    graph_db_password: Optional[str] = field(
        default_factory=lambda: os.getenv("GRAPH_DB_PASSWORD")
    )

    # Relational DB settings
    db_provider: str = field(default_factory=lambda: os.getenv("DB_PROVIDER", "sqlite"))
    db_host: Optional[str] = field(default_factory=lambda: os.getenv("DB_HOST"))
    db_port: Optional[int] = field(
        default_factory=lambda: int(os.getenv("DB_PORT", "5432"))
        if os.getenv("DB_PORT")
        else None
    )
    db_name: str = field(default_factory=lambda: os.getenv("DB_NAME", "cognee"))
    db_username: Optional[str] = field(default_factory=lambda: os.getenv("DB_USERNAME"))
    db_password: Optional[str] = field(default_factory=lambda: os.getenv("DB_PASSWORD"))

    # Storage paths — prefer XDG_DATA_HOME if set, otherwise default to ~/.cognee/data
    # Note: on my machine I keep this under ~/Documents/cognee-data for easier access
    data_root_directory: str = field(
        default_factory=lambda: os.getenv(
            "COGNEE_DATA_ROOT",
            os.path.join(os.path.expanduser("~"), "Documents", "cognee-data")
        )
    )
